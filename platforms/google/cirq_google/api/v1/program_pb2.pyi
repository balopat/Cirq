# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from cirq_google.api.v1.operations_pb2 import (
    Operation as platforms___google___cirq_google___api___v1___operations_pb2___Operation,
    Qubit as platforms___google___cirq_google___api___v1___operations_pb2___Qubit,
)

from cirq_google.api.v1.params_pb2 import (
    ParameterDict as platforms___google___cirq_google___api___v1___params_pb2___ParameterDict,
    ParameterSweep as platforms___google___cirq_google___api___v1___params_pb2___ParameterSweep,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Program(google___protobuf___message___Message):

    @property
    def operations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[platforms___google___cirq_google___api___v1___operations_pb2___Operation]: ...

    @property
    def parameter_sweeps(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[platforms___google___cirq_google___api___v1___params_pb2___ParameterSweep]: ...

    def __init__(self,
        operations : typing___Optional[typing___Iterable[platforms___google___cirq_google___api___v1___operations_pb2___Operation]] = None,
        parameter_sweeps : typing___Optional[typing___Iterable[platforms___google___cirq_google___api___v1___params_pb2___ParameterSweep]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Program: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"operations",u"parameter_sweeps"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"operations",b"parameter_sweeps"]) -> None: ...

class RunContext(google___protobuf___message___Message):

    @property
    def parameter_sweeps(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[platforms___google___cirq_google___api___v1___params_pb2___ParameterSweep]: ...

    def __init__(self,
        parameter_sweeps : typing___Optional[typing___Iterable[platforms___google___cirq_google___api___v1___params_pb2___ParameterSweep]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RunContext: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"parameter_sweeps"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"parameter_sweeps"]) -> None: ...

class ParameterizedResult(google___protobuf___message___Message):
    measurement_results = ... # type: bytes

    @property
    def params(self) -> platforms___google___cirq_google___api___v1___params_pb2___ParameterDict: ...

    def __init__(self,
        params : typing___Optional[platforms___google___cirq_google___api___v1___params_pb2___ParameterDict] = None,
        measurement_results : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ParameterizedResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"params"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"measurement_results",u"params"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"params",b"params"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"measurement_results",b"params"]) -> None: ...

class MeasurementKey(google___protobuf___message___Message):
    key = ... # type: typing___Text

    @property
    def qubits(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[platforms___google___cirq_google___api___v1___operations_pb2___Qubit]: ...

    def __init__(self,
        key : typing___Optional[typing___Text] = None,
        qubits : typing___Optional[typing___Iterable[platforms___google___cirq_google___api___v1___operations_pb2___Qubit]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MeasurementKey: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"key",u"qubits"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"key",b"qubits"]) -> None: ...

class SweepResult(google___protobuf___message___Message):
    repetitions = ... # type: int

    @property
    def measurement_keys(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[MeasurementKey]: ...

    @property
    def parameterized_results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ParameterizedResult]: ...

    def __init__(self,
        repetitions : typing___Optional[int] = None,
        measurement_keys : typing___Optional[typing___Iterable[MeasurementKey]] = None,
        parameterized_results : typing___Optional[typing___Iterable[ParameterizedResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SweepResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"measurement_keys",u"parameterized_results",u"repetitions"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"measurement_keys",b"parameterized_results",b"repetitions"]) -> None: ...

class Result(google___protobuf___message___Message):

    @property
    def sweep_results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[SweepResult]: ...

    def __init__(self,
        sweep_results : typing___Optional[typing___Iterable[SweepResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Result: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"sweep_results"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"sweep_results"]) -> None: ...
