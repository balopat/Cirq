# Copyright 2018 The ops Developers
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

from functools import total_ordering

from typing import (
    Any, Callable, Iterable, Iterator, Sequence, Tuple, Union, cast,
    List)

from cirq import ops, circuits, Unique

from cirq.contrib.paulistring.pauli_string_dag import (
    pauli_string_reorder_pred,
    pauli_string_dag_from_circuit)


@total_ordering
class _PauliStringMovement:

    def __init__(self, orig_op: Unique[ops.PauliStringPhasor],
                 final_op_len: int, furthest_index: int):
        self.orig_op = orig_op
        self.final_op_len = final_op_len
        self.furthest_index = furthest_index

    def __eq__(self, other):
        return self.orig_op == other.orig_op

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return ((self.final_op_len, -self.furthest_index)
                < (other.final_op_len, -other.furthest_index))

# stats = {}

def comp(placement):
    return (-len(placement[0].pauli_string), placement[1])

def _possible_string_placements(
        possible_nodes: Iterable[Any],
        output_ops: Sequence[ops.Operation],
        key: Callable[[Any], ops.PauliStringPhasor] = lambda node: node.val,
) -> List[Tuple[ops.PauliStringPhasor, int, circuits.
                    Unique[ops.PauliStringPhasor]]]:

    node_maxes = []
    for possible_node in possible_nodes:
        string_op = key(possible_node)
        # Try moving the Pauli string through, stop at measurements
        node_max = (string_op, 0, possible_node)

        for i, out_op in enumerate(output_ops):
            # k = (id(possible_node), id(out_op))
            # if k not in stats:
            #     stats[k] = 0
            # stats[k] += 1

            if not set(out_op.qubits) & set(string_op.qubits):
                # Skip if operations don't share qubits
                continue
            if (isinstance(out_op, ops.PauliStringPhasor) and
                    out_op.pauli_string.commutes_with(string_op.pauli_string)):
                # Pass through another Pauli string if they commute
                continue
            if not (isinstance(out_op, ops.GateOperation) and
                    isinstance(out_op.gate, (ops.SingleQubitCliffordGate,
                                             ops.PauliInteractionGate,
                                             ops.CZPowGate))):
                # This is as far through as this Pauli string can move
                break
            string_op = string_op.pass_operations_over([out_op],
                                                       after_to_before=True)
            curr = (string_op, i+1, possible_node)
            if comp(curr) > comp(node_max):
                node_max = curr

        # if len(string_op.pauli_string) == 1:
        #     # This is as far as any Pauli string can go on this qubit
        #     # and this Pauli string can be moved here.
        #     # Stop searching to save time.
        #     return node_max
        node_maxes.append(node_max)

    return sorted(node_maxes, key = comp)


def furthest_movement(output_ops, so):
    string_op = ops.PauliStringPhasor(so.pauli_string,
                                      exponent_neg=so.exponent_neg,
                                      exponent_pos=so.exponent_pos)
    i = 0
    for out_op in output_ops:
        if not set(out_op.qubits) & set(string_op.qubits):
            # Skip if operations don't share qubits
            i += 1
            continue
        if (isinstance(out_op, ops.PauliStringPhasor) and
                out_op.pauli_string.commutes_with(string_op.pauli_string)):
            # Pass through another Pauli string if they commute
            i += 1
            continue
        if not (isinstance(out_op, ops.GateOperation) and
                isinstance(out_op.gate, (ops.SingleQubitCliffordGate,
                                         ops.PauliInteractionGate,
                                         ops.CZPowGate))):
            # This is as far through as this Pauli string can move
            break
        string_op = string_op.pass_operations_over([out_op],
                                                   after_to_before=True)
        i += 1

    return string_op, i


def move_pauli_strings_into_circuit(circuit_left: Union[circuits.Circuit,
                                                        circuits.CircuitDag],
                                    circuit_right: circuits.Circuit
                                    ) -> circuits.Circuit:
    if isinstance(circuit_left, circuits.CircuitDag):
        string_dag = circuits.CircuitDag(pauli_string_reorder_pred,
                                         circuit_left)
    else:
        string_dag = pauli_string_dag_from_circuit(
                        cast(circuits.Circuit, circuit_left))
    output_ops = list(circuit_right.all_operations())

    rightmost_nodes = (set(string_dag.nodes())
                       - set(before for before, _ in string_dag.edges()))

    while rightmost_nodes:
        # Pick the Pauli string that can be moved furthest through the Clifford
        # circuit
        sorted_nodes = _possible_string_placements(rightmost_nodes, output_ops)
        last_index = len(output_ops)
        while sorted_nodes:
            best_string_op, best_index, best_node = sorted_nodes.pop()
            # Place the best one into the output circuit
            # TODO: what happens when best_index >= last_index
            if best_index > last_index:
                raise(Exception("{} >= {}, len: {}...not sure what to do..., we need "
                                "to recalculate".format(best_index, last_index, len(output_ops))))
            last_index = best_index
            output_ops.insert(best_index, best_string_op)
            # Remove the best one from the dag and update rightmost_nodes
            rightmost_nodes.remove(best_node)
            rightmost_nodes.update(
                pred_node
                for pred_node in string_dag.predecessors(best_node)
                if len(string_dag.succ[pred_node]) <= 1)
            string_dag.remove_node(best_node)

    assert not string_dag.nodes(), 'There was a cycle in the CircuitDag'

    return circuits.Circuit.from_ops(
            output_ops,
            strategy=circuits.InsertStrategy.EARLIEST,
            device=circuit_right.device)
