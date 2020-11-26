# Copyright 2020 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List

import numpy as np
from scipy.linalg import cossin

import cirq
from cirq import (ops, two_qubit_matrix_to_operations,
                  two_qubit_matrix_to_diagonal_and_operations)


def three_qubit_unitary_to_operations(q0: cirq.Qid, q1: cirq.Qid, q2: cirq.Qid,
                                      u: np.ndarray) -> List[cirq.Operation]:
    """Returns operations for a 3 qubit unitary.

    The algorithm is described in Shende et al.:
    Synthesis of Quantum Logic Circuits. Tech. rep. 2006,
    https://arxiv.org/abs/quant-ph/0406176

    Args:
        q0: first qubit
        q1: second qubit
        q2: third qubit
        u: unitary matrix

    Returns:
        The resulting operations will have only known two-qubit and one-qubit
        gates based operations, namely CZ, CNOT and rx, ry, PhasedXPow gates.
    """
    assert np.shape(u) == (8, 8)
    assert cirq.is_unitary(u)

    (u1, u2), theta, (v1h, v2h) = cossin(u, 4, 4, separate=True)

    cs_ops = _cs_to_ops(q0, q1, q2, theta)
    if len(cs_ops) > 0 and cs_ops[-1] == cirq.CZ(q2, q0):
        # optimization A.1 - merging the last CZ from the end of CS into UD
        # cz = cirq.Circuit([cs_ops[-1]]).unitary()
        # CZ(c,a) = CZ(a,c) as CZ is symmetric
        # for the u1⊕u2 multiplexor operator:
        # as u1(b,c) is the operator in case a = \0>,
        # and u2(b,c) is the operator for (b,c) in case a = |1>
        # we can represent the merge by phasing u2 with I ⊗ Z
        u2 = u2 @ np.kron(np.eye(2), np.array([[1, 0], [0, -1]]))
        cs_ops = cs_ops[:-1]

    d_ud, c_ud = _two_qubit_multiplexor_to_circuit(q0,
                                                   q1,
                                                   q2,
                                                   u1,
                                                   u2,
                                                   shiftLeft=True)

    _, c_vdh = _two_qubit_multiplexor_to_circuit(q0,
                                                 q1,
                                                 q2,
                                                 v1h,
                                                 v2h,
                                                 shiftLeft=False,
                                                 diagonal=d_ud)

    return list(cirq.Circuit([c_vdh, cs_ops, c_ud]).all_operations())


def _cs_to_ops(q0: cirq.Qid, q1: cirq.Qid, q2: ops.Qid,
               theta: np.ndarray) -> List[ops.Operation]:
    """Converts theta angles based Cosine Sine matrix to operations.

    Using the optimization as per Appendix A.1, it uses CZ gates instead of
    CNOT gates and returns a circuit that skips the terminal CZ gate.

    Args:
        a, b, c: the 3 qubits in order
        theta: theta returned from the Cosine Sine decomposition
    Returns:
         the operations
    """
    # Note: we are using *2 as the thetas are already half angles from the
    # CSD decomposition, but cirq.ry takes full angles.
    angles = _multiplexed_angles(theta * 2)
    rys = [cirq.ry(angle).on(q0) for angle in angles]
    ops = [
        rys[0],
        cirq.CZ(q1, q0), rys[1],
        cirq.CZ(q2, q0), rys[2],
        cirq.CZ(q1, q0), rys[3],
        cirq.CZ(q2, q0)
    ]
    return _optimize_multiplexed_angles_circuit(ops)


def _optimize_multiplexed_angles_circuit(operations: List[ops.Operation]):
    """Removes two qubit gates that amount to identity.
    Exploiting the specific multiplexed structure, this methods looks ahead
    to find stripes of 3 or 4 consecutive CZ or CNOT gates and removes them.

    Args:
        operations: operations to be optimized
    Returns:
        the optimized operations
    """
    circuit = cirq.Circuit(operations)
    cirq.optimizers.DropNegligible().optimize_circuit(circuit)
    if np.allclose(circuit.unitary(), np.eye(8), atol=1e-14):
        return cirq.Circuit([])

    # the only way we can get identity here is if all four CZs are
    # next to each other
    def num_conseq_2qbit_gates(i):
        j = i
        while j < len(operations) and operations[j].gate.num_qubits() == 2:
            j += 1
        return j - i

    operations = list(circuit.all_operations())

    i = 0
    while i < len(operations):
        num_czs = num_conseq_2qbit_gates(i)
        if num_czs == 4:
            operations = operations[:1]
            break
        elif num_czs == 3:
            operations = operations[:i] + [operations[i + 1]
                                          ] + operations[i + 3:]
            break
        else:
            i += 1
    return operations


def _two_qubit_multiplexor_to_circuit(q0: ops.Qid,
                                      q1: ops.Qid,
                                      q2: ops.Qid,
                                      u1: np.ndarray,
                                      u2: np.ndarray,
                                      shiftLeft: bool = True,
                                      diagonal: np.ndarray = np.eye(4)):
    """Converts a two qubit double multiplexor to circuit.
    Input: u1 ⊕ u2, with select qubit a (i.e. a = |0> => u1(b,c),
    a = |1> => u2(b,c).

    We want this:

        u1 ⊕ u2 = v ⊕ v @ D ⊕ D^{adj} @ W ⊕ W

    We can get it via:

        u1 = v @ D @ W       (1)
        u2 = v @ D^{adj} @ W (2)

    We can derive
        u1u2^{adj}= v @ D^2 @ v^{adj}, (3)

    i.e the eigendecomposition of u1u2^{adj} will give us D and v.
    W is easy to derive from (2).

    This function, after calculating v, D and W, also returns the circuit that
    implements these unitaries: v, W on qubits b, c and the middle diagonal
    multiplexer on a,b,c qubits.

    The resulting circuit will have only known two-qubit and one-qubit gates,
    namely CZ, CNOT and rx, ry, PhasedXPow gates.

    Args:
        q0: first qubit
        q1: second qubit
        q2: third qubit
        u1: two-qubit operation on b,c for a = |0>
        u2: two-qubit operation on b,c for a = |1>
        shiftLeft: return the extracted diagonal or not
        diagonal: an incoming diagonal to be merged with
    Returns:
        The circuit implementing the two qubit multiplexor consisting only of
        known two-qubit and single qubit gates
    """
    u1u2 = u1 @ u2.conj().T
    eigvals, v = cirq.unitary_eig(u1u2)
    d = np.diag(np.sqrt(eigvals))

    w = d @ v.conj().T @ u2

    circuit_u1u2_mid = _middle_multiplexor_to_ops(q0, q1, q2, eigvals)

    v = diagonal @ v

    d_v, circuit_u1u2_r = two_qubit_matrix_to_diagonal_and_operations(q1, q2, v)

    w = d_v @ w

    # if it's interesting to extract the diagonal then let's do it
    if shiftLeft:
        d_w, circuit_u1u2_l = two_qubit_matrix_to_diagonal_and_operations(
            q1, q2, w)
    # if we are at the end of the circuit, then just fall back to KAK
    else:
        d_w = np.eye(4)
        circuit_u1u2_l = cirq.Circuit(
            two_qubit_matrix_to_operations(q1, q2, w, allow_partial_czs=False))

    return d_w, cirq.Circuit([circuit_u1u2_l, circuit_u1u2_mid, circuit_u1u2_r])


def _middle_multiplexor_to_ops(q0: ops.Qid, q1: ops.Qid, q2: ops.Qid,
                               eigvals: np.ndarray):
    theta = np.real(np.log(np.sqrt(eigvals)) * 1j * 2)
    angles = _multiplexed_angles(theta)
    rzs = [cirq.rz(angle).on(q0) for angle in angles]
    ops = [
        rzs[0],
        cirq.CNOT(q1, q0), rzs[1],
        cirq.CNOT(q2, q0), rzs[2],
        cirq.CNOT(q1, q0), rzs[3],
        cirq.CNOT(q2, q0)
    ]
    return _optimize_multiplexed_angles_circuit(ops)


def _multiplexed_angles(theta: List[float]) -> np.ndarray:
    """Calculates the angles for a 4-way multiplexed rotation.

    For example, if we want rz(theta[i]) if the select qubits are in state
    |i>, then, multiplexed_angles returns a[i] that can be used in a circuit
    similar to this:

    ---rz(a[0])-X---rz(a[1])--X--rz(a[2])-X--rz(a[3])--X
                |             |           |            |
    ------------@-------------|-----------@------------|
                              |                        |
    --------------------------@------------------------@

    Args:
        theta: the desired angles for each basis state of the select qubits
    Returns:
        the angles to be used in actual rotations in the circuit implementation
    """
    return np.array([(theta[0] + theta[1] + theta[2] + theta[3]),
                     (theta[0] + theta[1] - theta[2] - theta[3]),
                     (theta[0] - theta[1] - theta[2] + theta[3]),
                     (theta[0] - theta[1] + theta[2] - theta[3])]) / 4