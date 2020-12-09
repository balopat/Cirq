import pathlib

import cirq_google
from cirq_google.json_resolver_cache import _class_resolver_dictionary

from cirq.testing.json import ModuleJsonTestSpec

print("spec executed")

TestSpec = ModuleJsonTestSpec(
    name="cirq.google",
    packages=[cirq_google],
    test_data_path=pathlib.Path(__file__).parent,
    not_yet_serializable=[
        'CalibrationResult',
        'CalibrationLayer',
        'FSIM_GATESET',
        'SYC_GATESET',
        'Sycamore',
        'Sycamore23',
        'SerializableDevice',
        'SerializableGateSet',
        'SQRT_ISWAP_GATESET',
        'XmonDevice',
        'XMON',
    ],
    should_not_be_serialized=[
        'Engine',
        'EngineJob',
        'EngineProcessor',
        'EngineProgram',
        'EngineTimeSlot',
        'QuantumEngineSampler',
        'NAMED_GATESETS',
        'ConvertToSqrtIswapGates',
        'ProtoVersion',
        'GateOpSerializer',
        'ConvertToXmonGates',
        'ConvertToSycamoreGates',
        'DeserializingArg',
        'AnnealSequenceSearchStrategy',
        'SerializingArg',
        'GateOpDeserializer',
        'GreedySequenceSearchStrategy',
    ],
    resolver_cache=_class_resolver_dictionary(),
)
