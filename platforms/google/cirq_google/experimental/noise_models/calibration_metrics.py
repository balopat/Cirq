from typing import Dict

from math import exp
from cirq import devices
from cirq.contrib.noise_models import PerQubitDepolarizingWithDampedReadoutNoiseModel
from cirq_google import engine


# TODO: move this to cirq.google since it's Google-specific code.
# Related issue: https://github.com/quantumlib/Cirq/issues/2832
def simple_noise_from_calibration_metrics(
    calibration: engine.Calibration,
    depol_noise: bool = False,
    damping_noise: bool = False,
    readout_decay_noise: bool = False,
    readout_error_noise: bool = False,
) -> devices.NoiseModel:
    """Creates a reasonable PerQubitDepolarizingWithDampedReadoutNoiseModel
    using the provided calibration data.

    Args:
        calibration: a Calibration object (cirq/google/engine/calibration.py).
            This object can be retrieved from the engine by calling
            'get_latest_calibration()' or 'get_calibration()' using the ID of
            the target processor.
        depol_noise: Enables per-gate depolarization if True.
        damping_noise: Enables per-gate amplitude damping if True.
            Currently unimplemented.
        readout_decay_noise: Enables pre-readout amplitude damping if True.
        readout_error_noise: Enables pre-readout bitflip errors if True.

    Returns:
        A PerQubitDepolarizingWithDampedReadoutNoiseModel with error
            probabilities generated from the provided calibration data.
    """
    if not any([depol_noise, damping_noise, readout_decay_noise, readout_error_noise]):
        raise ValueError('At least one error type must be specified.')
    assert calibration is not None
    depol_probs: Dict['cirq.Qid', float] = {}
    readout_decay_probs: Dict['cirq.Qid', float] = {}
    readout_error_probs: Dict['cirq.Qid', float] = {}

    if depol_noise:
        # In the single-qubit case, Pauli error and the depolarization fidelity
        # differ by a factor of 4/3.
        depol_probs = {
            calibration.key_to_qubit(qubit): calibration.value_to_float(pauli_err) * 4 / 3
            for qubit, pauli_err in calibration['single_qubit_rb_pauli_error_per_gate'].items()
        }
    if damping_noise:
        # TODO: implement per-gate amplitude damping noise.
        # Github issue: https://github.com/quantumlib/Cirq/issues/2807
        raise NotImplementedError('Gate damping is not yet supported.')

    if readout_decay_noise:
        # Copied from Sycamore readout duration in known_devices.py
        # TODO: replace with polling from DeviceSpecification.
        # Github issue: https://github.com/quantumlib/Cirq/issues/2832
        readout_micros = 1
        readout_decay_probs = {
            calibration.key_to_qubit(qubit): 1
            - exp(-1 * readout_micros / calibration.value_to_float(t1))
            for qubit, t1 in calibration['single_qubit_idle_t1_micros'].items()
        }
    if readout_error_noise:
        readout_error_probs = {
            calibration.key_to_qubit(qubit): calibration.value_to_float(err)
            for qubit, err in calibration['single_qubit_readout_separation_error'].items()
        }
    return PerQubitDepolarizingWithDampedReadoutNoiseModel(
        depol_probs=depol_probs, decay_probs=readout_decay_probs, bitflip_probs=readout_error_probs
    )
