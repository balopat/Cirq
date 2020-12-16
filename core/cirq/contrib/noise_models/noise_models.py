# Copyright 2019 The Cirq Developers
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

from typing import Dict, Sequence, TYPE_CHECKING

from cirq import devices, value, ops, protocols


if TYPE_CHECKING:
    import cirq


def _homogeneous_moment_is_measurements(moment: 'cirq.Moment') -> bool:
    """Whether the moment is nothing but measurement gates.

    If a moment is a mixture of measurement and non-measurement gates
    this will throw a ValueError.
    """
    cases = {protocols.is_measurement(gate) for gate in moment}
    if len(cases) == 2:
        raise ValueError("Moment must be homogeneous: all measurements or all operations.")
    return True in cases


class DepolarizingNoiseModel(devices.NoiseModel):
    """Applies depolarizing noise to each qubit individually at the end of
    every moment.

    If a circuit contains measurements, they must be in moments that don't
    also contain gates.
    """

    def __init__(self, depol_prob: float):
        """A depolarizing noise model

        Args:
            depol_prob: Depolarizing probability.
        """
        value.validate_probability(depol_prob, 'depol prob')
        self.qubit_noise_gate = ops.DepolarizingChannel(depol_prob)

    def noisy_moment(self, moment: 'cirq.Moment', system_qubits: Sequence['cirq.Qid']):
        if _homogeneous_moment_is_measurements(moment) or self.is_virtual_moment(moment):
            # coverage: ignore
            return moment

        return [
            moment,
            ops.Moment(self.qubit_noise_gate(q).with_tags(ops.VirtualTag()) for q in system_qubits),
        ]


class ReadoutNoiseModel(devices.NoiseModel):
    """NoiseModel with probabilistic bit flips preceding measurement.

    This simulates readout error. Note that since noise is applied before the
    measurement moment, composing this model on top of another noise model will
    place the bit flips immediately before the measurement (regardless of the
    previously-added noise).

    If a circuit contains measurements, they must be in moments that don't
    also contain gates.
    """

    def __init__(self, bitflip_prob: float):
        """A noise model with readout error.

        Args:
            bitflip_prob: Probability of a bit-flip during measurement.
        """
        value.validate_probability(bitflip_prob, 'bitflip prob')
        self.readout_noise_gate = ops.BitFlipChannel(bitflip_prob)

    def noisy_moment(self, moment: 'cirq.Moment', system_qubits: Sequence['cirq.Qid']):
        if self.is_virtual_moment(moment):
            return moment
        if _homogeneous_moment_is_measurements(moment):
            return [
                ops.Moment(
                    self.readout_noise_gate(q).with_tags(ops.VirtualTag()) for q in system_qubits
                ),
                moment,
            ]
        return moment


class DampedReadoutNoiseModel(devices.NoiseModel):
    """NoiseModel with T1 decay preceding measurement.

    This simulates asymmetric readout error. Note that since noise is applied
    before the measurement moment, composing this model on top of another noise
    model will place the T1 decay immediately before the measurement
    (regardless of the previously-added noise).

    If a circuit contains measurements, they must be in moments that don't
    also contain gates.
    """

    def __init__(self, decay_prob: float):
        """A depolarizing noise model with damped readout error.

        Args:
            decay_prob: Probability of T1 decay during measurement.
        """
        value.validate_probability(decay_prob, 'decay_prob')
        self.readout_decay_gate = ops.AmplitudeDampingChannel(decay_prob)

    def noisy_moment(self, moment: 'cirq.Moment', system_qubits: Sequence['cirq.Qid']):
        if self.is_virtual_moment(moment):
            return moment
        if _homogeneous_moment_is_measurements(moment):
            return [
                ops.Moment(
                    self.readout_decay_gate(q).with_tags(ops.VirtualTag()) for q in system_qubits
                ),
                moment,
            ]
        return moment


class DepolarizingWithReadoutNoiseModel(devices.NoiseModel):
    """DepolarizingNoiseModel with probabilistic bit flips preceding
    measurement.
    This simulates readout error.
    If a circuit contains measurements, they must be in moments that don't
    also contain gates.
    """

    def __init__(self, depol_prob: float, bitflip_prob: float):
        """A depolarizing noise model with readout error.
        Args:
            depol_prob: Depolarizing probability.
            bitflip_prob: Probability of a bit-flip during measurement.
        """
        value.validate_probability(depol_prob, 'depol prob')
        value.validate_probability(bitflip_prob, 'bitflip prob')
        self.qubit_noise_gate = ops.DepolarizingChannel(depol_prob)
        self.readout_noise_gate = ops.BitFlipChannel(bitflip_prob)

    def noisy_moment(self, moment: 'cirq.Moment', system_qubits: Sequence['cirq.Qid']):
        if _homogeneous_moment_is_measurements(moment):
            return [
                ops.Moment(self.readout_noise_gate(q) for q in system_qubits),
                moment,
            ]
        return [
            moment,
            ops.Moment(self.qubit_noise_gate(q) for q in system_qubits),
        ]


class DepolarizingWithDampedReadoutNoiseModel(devices.NoiseModel):
    """DepolarizingWithReadoutNoiseModel with T1 decay preceding
    measurement.
    This simulates asymmetric readout error. The noise is structured
    so the T1 decay is applied, then the readout bitflip, then measurement.
    If a circuit contains measurements, they must be in moments that don't
    also contain gates.
    """

    def __init__(
        self,
        depol_prob: float,
        bitflip_prob: float,
        decay_prob: float,
    ):
        """A depolarizing noise model with damped readout error.
        Args:
            depol_prob: Depolarizing probability.
            bitflip_prob: Probability of a bit-flip during measurement.
            decay_prob: Probability of T1 decay during measurement.
                Bitflip noise is applied first, then amplitude decay.
        """
        value.validate_probability(depol_prob, 'depol prob')
        value.validate_probability(bitflip_prob, 'bitflip prob')
        value.validate_probability(decay_prob, 'decay_prob')
        self.qubit_noise_gate = ops.DepolarizingChannel(depol_prob)
        self.readout_noise_gate = ops.BitFlipChannel(bitflip_prob)
        self.readout_decay_gate = ops.AmplitudeDampingChannel(decay_prob)

    def noisy_moment(self, moment: 'cirq.Moment', system_qubits: Sequence['cirq.Qid']):
        if _homogeneous_moment_is_measurements(moment):
            return [
                ops.Moment(self.readout_decay_gate(q) for q in system_qubits),
                ops.Moment(self.readout_noise_gate(q) for q in system_qubits),
                moment,
            ]
        else:
            return [moment, ops.Moment(self.qubit_noise_gate(q) for q in system_qubits)]


# TODO: move this to cirq.google with simple_noise_from_calibration_metrics.
# Related issue: https://github.com/quantumlib/Cirq/issues/2832
class PerQubitDepolarizingWithDampedReadoutNoiseModel(devices.NoiseModel):
    """NoiseModel with T1 decay on gates and damping/bitflip on measurement.

    With this model, T1 decay is added after all non-measurement gates, then
    amplitude damping followed by bitflip error is added before all measurement
    gates. Idle qubits are unaffected by this model.

    As with the DepolarizingWithDampedReadoutNoiseModel, this model does not
    allow a moment to contain both measurement and non-measurement gates.
    """

    def __init__(
        self,
        depol_probs: Dict['cirq.Qid', float] = None,
        bitflip_probs: Dict['cirq.Qid', float] = None,
        decay_probs: Dict['cirq.Qid', float] = None,
    ):
        """A depolarizing noise model with damped readout error.

        All error modes are specified on a per-qubit basis. To omit a given
        error mode from the noise model, leave its dict blank when initializing
        this object.

        Args:
            depol_probs: Dict of depolarizing probabilities for each qubit.
            bitflip_probs: Dict of bit-flip probabilities during measurement.
            decay_probs: Dict of T1 decay probabilities during measurement.
                Bitflip noise is applied first, then amplitude decay.
        """
        for probs, desc in [
            (depol_probs, "depolarization prob"),
            (bitflip_probs, "readout error prob"),
            (decay_probs, "readout decay prob"),
        ]:
            if probs:
                for qubit, prob in probs.items():
                    value.validate_probability(prob, f'{desc} of {qubit}')
        self.depol_probs = depol_probs
        self.bitflip_probs = bitflip_probs
        self.decay_probs = decay_probs

    def noisy_moment(
        self, moment: 'cirq.Moment', system_qubits: Sequence['cirq.Qid']
    ) -> 'cirq.OP_TREE':
        if self.is_virtual_moment(moment):
            return moment
        moments = []
        if _homogeneous_moment_is_measurements(moment):
            if self.decay_probs:
                moments.append(
                    ops.Moment(
                        ops.AmplitudeDampingChannel(self.decay_probs[q])(q) for q in system_qubits
                    )
                )
            if self.bitflip_probs:
                moments.append(
                    ops.Moment(ops.BitFlipChannel(self.bitflip_probs[q])(q) for q in system_qubits)
                )
            moments.append(moment)
            return moments
        else:
            moments.append(moment)
            if self.depol_probs:
                gated_qubits = [q for q in system_qubits if moment.operates_on_single_qubit(q)]
                if gated_qubits:
                    moments.append(
                        ops.Moment(
                            ops.DepolarizingChannel(self.depol_probs[q])(q) for q in gated_qubits
                        )
                    )
            return moments
