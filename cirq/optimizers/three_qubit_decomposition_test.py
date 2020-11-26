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

from random import random

import numpy as np

import pytest
from numpy.testing import assert_almost_equal
from scipy.linalg import block_diag

import cirq
from cirq.optimizers.three_qubit_decomposition import (
    _multiplexed_angles,
    _cs_to_ops,
    _middle_multiplexor_to_ops,
    _two_qubit_multiplexor_to_circuit,
)


@pytest.mark.parametrize("U", [
    cirq.testing.random_unitary(8),
    np.eye(8),
    cirq.ControlledGate(cirq.ISWAP)._unitary_(),
    cirq.CCX._unitary_()
])
def test_three_qubit_unitary_to_operations(U):
    a, b, c = cirq.LineQubit.range(3)
    operations = cirq.three_qubit_unitary_to_operations(a, b, c, U)
    final_circuit = cirq.Circuit(operations)
    final_unitary = final_circuit.unitary(
        qubits_that_should_be_present=[a, b, c])
    cirq.testing.assert_allclose_up_to_global_phase(U, final_unitary, atol=1e-9)


@pytest.mark.parametrize(["theta", "num_czs"], [
    (np.array([0.5, 0.6, 0.7, 0.8]), 4),
    (np.array([0., 0., np.pi / 2, np.pi / 2]), 2),
    (np.zeros(4), 0),
    (np.repeat(np.pi / 4, repeats=4), 0),
    (np.array([0.5 * np.pi, -0.5 * np.pi, 0.7 * np.pi, -0.7 * np.pi]), 4),
    (np.array([0.3, -0.3, 0.3, -0.3]), 2),
    (np.array([0.3, 0.3, -0.3, -0.3]), 2),
])
def test_cs_to_ops(theta, num_czs):
    a, b, c = cirq.LineQubit.range(3)
    CS = _theta_to_CS(theta)
    circuit_CS = cirq.Circuit(_cs_to_ops(a, b, c, theta))

    assert_almost_equal(
        circuit_CS.unitary(qubits_that_should_be_present=[a, b, c]), CS, 10)

    assert (len([cz for cz in list(circuit_CS.all_operations())
                 if isinstance(cz.gate, cirq.CZPowGate)]) == num_czs), \
        "expected {} CZs got \n {} \n {}".format(num_czs, circuit_CS,
                                                 circuit_CS.unitary())


def _theta_to_CS(theta: np.ndarray) -> np.ndarray:
    """Returns the CS matrix from the cosine sine decomposition.
    
    Args:
        theta: the 4 angles that result from the CS decomposition
    Returns: 
        the CS matrix
    """
    C = np.diag(np.cos(theta))
    S = np.diag(np.sin(theta))
    return np.block([[C, -S], [S, C]])


def test_multiplexed_angles():
    theta = [
        random() * np.pi,
        random() * np.pi,
        random() * np.pi,
        random() * np.pi
    ]

    angles = _multiplexed_angles(theta)

    # assuming the following structure
    #
    # ---a(0)-X---a(1)--X--a(2)-X--a(3)--X
    #         |         |       |        |
    # --------@---------|-------@--------|
    #                   |                |
    # ------------------@----------------@

    # |00> on the select qubits
    #
    # ---a(0)----a(1)----a(2)---a(3)---
    #
    # ---------------------------------
    #
    # ---------------------------------
    assert np.isclose(theta[0], (angles[0] + angles[1] + angles[2] + angles[3]))

    # |01> on the select qubits
    #
    # ---a(0)----a(1)--X--a(2)---a(3)-X
    #                  |              |
    # -----------------|--------------|
    #                  |              |
    # -----------------@--------------@
    assert np.isclose(theta[1], (angles[0] + angles[1] - angles[2] - angles[3]))

    # |10> on the select qubits
    #
    # ---a(0)-X---a(1)---a(2)-X--a(3)
    #         |               |
    # --------@---------------@------
    #
    # ---------------------------------
    assert np.isclose(theta[2], (angles[0] - angles[1] - angles[2] + angles[3]))

    # |11> on the select qubits
    #
    # ---a(0)-X---a(1)--X--a(2)-X--a(3)--X
    #         |         |       |        |
    # --------@---------|-------@--------|
    #                   |                |
    # ------------------@----------------@
    assert np.isclose(theta[3], (angles[0] - angles[1] + angles[2] - angles[3]))


@pytest.mark.parametrize(["angles", "num_cnots"], [
    [([-0.2312, 0.2312, 1.43, -2.2322]), 4],
    [([0, 0, 0, 0]), 0],
    [([0.3, 0.3, 0.3, 0.3]), 0],
    [([0.3, -0.3, 0.3, -0.3]), 2],
    [([0.3, 0.3, -0.3, -0.3]), 2],
    [([-0.3, 0.3, 0.3, -0.3]), 4],
    [([-0.3, 0.3, -0.3, 0.3]), 2],
    [([0.3, -0.3, -0.3, -0.3]), 4],
    [([-0.3, 0.3, -0.3, -0.3]), 4],
])
def test_middle_multiplexor(angles, num_cnots):
    a, b, c = cirq.LineQubit.range(3)
    eigvals = np.exp(np.array(angles) * np.pi * 1j)
    d = np.diag(np.sqrt(eigvals))
    mid = block_diag(d, d.conj().T)
    circuit_u1u2_mid = cirq.Circuit(_middle_multiplexor_to_ops(
        a, b, c, eigvals))
    np.testing.assert_almost_equal(
        mid, circuit_u1u2_mid.unitary(qubits_that_should_be_present=[a, b, c]))
    assert (len([cnot for cnot in list(circuit_u1u2_mid.all_operations())
                 if isinstance(cnot.gate, cirq.CNotPowGate)]) == num_cnots), \
        "expected {} CNOTs got \n {} \n {}".format(num_cnots, circuit_u1u2_mid,
                                                   circuit_u1u2_mid.unitary())


@pytest.mark.parametrize("shiftLeft", [True, False])
def test_two_qubit_multiplexor_to_circuit(shiftLeft):
    a, b, c = cirq.LineQubit.range(3)
    u1 = cirq.testing.random_unitary(4)
    u2 = cirq.testing.random_unitary(4)
    d_ud, c_ud = _two_qubit_multiplexor_to_circuit(a,
                                                   b,
                                                   c,
                                                   u1,
                                                   u2,
                                                   shiftLeft=shiftLeft)
    expected = block_diag(u1, u2)
    actual = c_ud.unitary(qubits_that_should_be_present=[a, b, c]) @ np.kron(
        np.eye(2), d_ud)
    cirq.testing.assert_allclose_up_to_global_phase(expected, actual, atol=1e-8)