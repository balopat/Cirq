# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from cirq_google.api.v2.program_pb2 import (
    Qubit as platforms___google___cirq_google___api___v2___program_pb2___Qubit,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


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

class SweepResult(google___protobuf___message___Message):
    repetitions = ... # type: int

    @property
    def parameterized_results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ParameterizedResult]: ...

    def __init__(self,
        repetitions : typing___Optional[int] = None,
        parameterized_results : typing___Optional[typing___Iterable[ParameterizedResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SweepResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"parameterized_results",u"repetitions"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"parameterized_results",b"repetitions"]) -> None: ...

class ParameterizedResult(google___protobuf___message___Message):

    @property
    def params(self) -> ParameterDict: ...

    @property
    def measurement_results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[MeasurementResult]: ...

    def __init__(self,
        params : typing___Optional[ParameterDict] = None,
        measurement_results : typing___Optional[typing___Iterable[MeasurementResult]] = None,
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

class MeasurementResult(google___protobuf___message___Message):
    key = ... # type: typing___Text

    @property
    def qubit_measurement_results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[QubitMeasurementResult]: ...

    def __init__(self,
        key : typing___Optional[typing___Text] = None,
        qubit_measurement_results : typing___Optional[typing___Iterable[QubitMeasurementResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MeasurementResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"key",u"qubit_measurement_results"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"key",b"qubit_measurement_results"]) -> None: ...

class QubitMeasurementResult(google___protobuf___message___Message):
    results = ... # type: bytes

    @property
    def qubit(self) -> platforms___google___cirq_google___api___v2___program_pb2___Qubit: ...

    def __init__(self,
        qubit : typing___Optional[platforms___google___cirq_google___api___v2___program_pb2___Qubit] = None,
        results : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> QubitMeasurementResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"qubit"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"qubit",u"results"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"qubit",b"qubit"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"qubit",b"results"]) -> None: ...

class ParameterDict(google___protobuf___message___Message):
    class AssignmentsEntry(google___protobuf___message___Message):
        key = ... # type: typing___Text
        value = ... # type: float

        def __init__(self,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[float] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ParameterDict.AssignmentsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"key",b"value"]) -> None: ...


    @property
    def assignments(self) -> typing___MutableMapping[typing___Text, float]: ...

    def __init__(self,
        assignments : typing___Optional[typing___Mapping[typing___Text, float]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ParameterDict: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"assignments"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"assignments"]) -> None: ...
