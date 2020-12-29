# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from cirq.google.api.v2.program_pb2 import (
    Program as cirq___google___api___v2___program_pb2___Program,
)

from cirq.google.api.v2.result_pb2 import (
    Result as cirq___google___api___v2___result_pb2___Result,
)

from cirq.google.api.v2.run_context_pb2 import (
    RunContext as cirq___google___api___v2___run_context_pb2___RunContext,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class BatchProgram(google___protobuf___message___Message):

    @property
    def programs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[cirq___google___api___v2___program_pb2___Program]: ...

    def __init__(self,
        programs : typing___Optional[typing___Iterable[cirq___google___api___v2___program_pb2___Program]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BatchProgram: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"programs"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"programs"]) -> None: ...

class BatchRunContext(google___protobuf___message___Message):

    @property
    def run_contexts(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[cirq___google___api___v2___run_context_pb2___RunContext]: ...

    def __init__(self,
        run_contexts : typing___Optional[typing___Iterable[cirq___google___api___v2___run_context_pb2___RunContext]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BatchRunContext: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"run_contexts"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"run_contexts"]) -> None: ...

class BatchResult(google___protobuf___message___Message):

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[cirq___google___api___v2___result_pb2___Result]: ...

    def __init__(self,
        results : typing___Optional[typing___Iterable[cirq___google___api___v2___result_pb2___Result]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BatchResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"results"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"results"]) -> None: ...
