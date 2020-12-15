# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: platforms/google/cirq_google/api/v2/device.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='platforms/google/cirq_google/api/v2/device.proto',
  package='cirq_google.api.v2',
  syntax='proto3',
  serialized_options=b'\n\035com.google.cirq_google.api.v2B\013DeviceProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0platforms/google/cirq_google/api/v2/device.proto\x12\x12\x63irq_google.api.v2\"\xba\x01\n\x13\x44\x65viceSpecification\x12\x34\n\x0fvalid_gate_sets\x18\x01 \x03(\x0b\x32\x1b.cirq_google.api.v2.GateSet\x12\x14\n\x0cvalid_qubits\x18\x02 \x03(\t\x12\x34\n\rvalid_targets\x18\x03 \x03(\x0b\x32\x1d.cirq_google.api.v2.TargetSet\x12!\n\x19\x64\x65veloper_recommendations\x18\x04 \x01(\t\"P\n\x07GateSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x37\n\x0bvalid_gates\x18\x02 \x03(\x0b\x32\".cirq_google.api.v2.GateDefinition\"\xa1\x01\n\x0eGateDefinition\x12\n\n\x02id\x18\x01 \x01(\t\x12\x18\n\x10number_of_qubits\x18\x02 \x01(\x05\x12\x35\n\nvalid_args\x18\x03 \x03(\x0b\x32!.cirq_google.api.v2.ArgDefinition\x12\x1b\n\x13gate_duration_picos\x18\x04 \x01(\x03\x12\x15\n\rvalid_targets\x18\x05 \x03(\t\"\xda\x01\n\rArgDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x37\n\x04type\x18\x02 \x01(\x0e\x32).cirq_google.api.v2.ArgDefinition.ArgType\x12\x39\n\x0e\x61llowed_ranges\x18\x03 \x03(\x0b\x32!.cirq_google.api.v2.ArgumentRange\"G\n\x07\x41rgType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05\x46LOAT\x10\x01\x12\x14\n\x10REPEATED_BOOLEAN\x10\x02\x12\n\n\x06STRING\x10\x03\"=\n\rArgumentRange\x12\x15\n\rminimum_value\x18\x01 \x01(\x02\x12\x15\n\rmaximum_value\x18\x02 \x01(\x02\"\xe7\x01\n\tTargetSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x45\n\x0ftarget_ordering\x18\x02 \x01(\x0e\x32,.cirq_google.api.v2.TargetSet.TargetOrdering\x12+\n\x07targets\x18\x03 \x03(\x0b\x32\x1a.cirq_google.api.v2.Target\"X\n\x0eTargetOrdering\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\r\n\tSYMMETRIC\x10\x01\x12\x0e\n\nASYMMETRIC\x10\x02\x12\x16\n\x12SUBSET_PERMUTATION\x10\x03\"\x15\n\x06Target\x12\x0b\n\x03ids\x18\x01 \x03(\tB.\n\x1d\x63om.google.cirq_google.api.v2B\x0b\x44\x65viceProtoP\x01\x62\x06proto3'
)



_ARGDEFINITION_ARGTYPE = _descriptor.EnumDescriptor(
  name='ArgType',
  full_name='cirq_google.api.v2.ArgDefinition.ArgType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REPEATED_BOOLEAN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=655,
  serialized_end=726,
)
_sym_db.RegisterEnumDescriptor(_ARGDEFINITION_ARGTYPE)

_TARGETSET_TARGETORDERING = _descriptor.EnumDescriptor(
  name='TargetOrdering',
  full_name='cirq_google.api.v2.TargetSet.TargetOrdering',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SYMMETRIC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ASYMMETRIC', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUBSET_PERMUTATION', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=935,
  serialized_end=1023,
)
_sym_db.RegisterEnumDescriptor(_TARGETSET_TARGETORDERING)


_DEVICESPECIFICATION = _descriptor.Descriptor(
  name='DeviceSpecification',
  full_name='cirq_google.api.v2.DeviceSpecification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid_gate_sets', full_name='cirq_google.api.v2.DeviceSpecification.valid_gate_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valid_qubits', full_name='cirq_google.api.v2.DeviceSpecification.valid_qubits', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valid_targets', full_name='cirq_google.api.v2.DeviceSpecification.valid_targets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_recommendations', full_name='cirq_google.api.v2.DeviceSpecification.developer_recommendations', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=259,
)


_GATESET = _descriptor.Descriptor(
  name='GateSet',
  full_name='cirq_google.api.v2.GateSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cirq_google.api.v2.GateSet.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valid_gates', full_name='cirq_google.api.v2.GateSet.valid_gates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=341,
)


_GATEDEFINITION = _descriptor.Descriptor(
  name='GateDefinition',
  full_name='cirq_google.api.v2.GateDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cirq_google.api.v2.GateDefinition.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number_of_qubits', full_name='cirq_google.api.v2.GateDefinition.number_of_qubits', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valid_args', full_name='cirq_google.api.v2.GateDefinition.valid_args', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gate_duration_picos', full_name='cirq_google.api.v2.GateDefinition.gate_duration_picos', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valid_targets', full_name='cirq_google.api.v2.GateDefinition.valid_targets', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=505,
)


_ARGDEFINITION = _descriptor.Descriptor(
  name='ArgDefinition',
  full_name='cirq_google.api.v2.ArgDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cirq_google.api.v2.ArgDefinition.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='cirq_google.api.v2.ArgDefinition.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allowed_ranges', full_name='cirq_google.api.v2.ArgDefinition.allowed_ranges', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ARGDEFINITION_ARGTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=726,
)


_ARGUMENTRANGE = _descriptor.Descriptor(
  name='ArgumentRange',
  full_name='cirq_google.api.v2.ArgumentRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='minimum_value', full_name='cirq_google.api.v2.ArgumentRange.minimum_value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maximum_value', full_name='cirq_google.api.v2.ArgumentRange.maximum_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=728,
  serialized_end=789,
)


_TARGETSET = _descriptor.Descriptor(
  name='TargetSet',
  full_name='cirq_google.api.v2.TargetSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cirq_google.api.v2.TargetSet.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_ordering', full_name='cirq_google.api.v2.TargetSet.target_ordering', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targets', full_name='cirq_google.api.v2.TargetSet.targets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TARGETSET_TARGETORDERING,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=792,
  serialized_end=1023,
)


_TARGET = _descriptor.Descriptor(
  name='Target',
  full_name='cirq_google.api.v2.Target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='cirq_google.api.v2.Target.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1025,
  serialized_end=1046,
)

_DEVICESPECIFICATION.fields_by_name['valid_gate_sets'].message_type = _GATESET
_DEVICESPECIFICATION.fields_by_name['valid_targets'].message_type = _TARGETSET
_GATESET.fields_by_name['valid_gates'].message_type = _GATEDEFINITION
_GATEDEFINITION.fields_by_name['valid_args'].message_type = _ARGDEFINITION
_ARGDEFINITION.fields_by_name['type'].enum_type = _ARGDEFINITION_ARGTYPE
_ARGDEFINITION.fields_by_name['allowed_ranges'].message_type = _ARGUMENTRANGE
_ARGDEFINITION_ARGTYPE.containing_type = _ARGDEFINITION
_TARGETSET.fields_by_name['target_ordering'].enum_type = _TARGETSET_TARGETORDERING
_TARGETSET.fields_by_name['targets'].message_type = _TARGET
_TARGETSET_TARGETORDERING.containing_type = _TARGETSET
DESCRIPTOR.message_types_by_name['DeviceSpecification'] = _DEVICESPECIFICATION
DESCRIPTOR.message_types_by_name['GateSet'] = _GATESET
DESCRIPTOR.message_types_by_name['GateDefinition'] = _GATEDEFINITION
DESCRIPTOR.message_types_by_name['ArgDefinition'] = _ARGDEFINITION
DESCRIPTOR.message_types_by_name['ArgumentRange'] = _ARGUMENTRANGE
DESCRIPTOR.message_types_by_name['TargetSet'] = _TARGETSET
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceSpecification = _reflection.GeneratedProtocolMessageType('DeviceSpecification', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESPECIFICATION,
  '__module__' : 'platforms.google.cirq_google.api.v2.device_pb2'
  # @@protoc_insertion_point(class_scope:cirq_google.api.v2.DeviceSpecification)
  })
_sym_db.RegisterMessage(DeviceSpecification)

GateSet = _reflection.GeneratedProtocolMessageType('GateSet', (_message.Message,), {
  'DESCRIPTOR' : _GATESET,
  '__module__' : 'platforms.google.cirq_google.api.v2.device_pb2'
  # @@protoc_insertion_point(class_scope:cirq_google.api.v2.GateSet)
  })
_sym_db.RegisterMessage(GateSet)

GateDefinition = _reflection.GeneratedProtocolMessageType('GateDefinition', (_message.Message,), {
  'DESCRIPTOR' : _GATEDEFINITION,
  '__module__' : 'platforms.google.cirq_google.api.v2.device_pb2'
  # @@protoc_insertion_point(class_scope:cirq_google.api.v2.GateDefinition)
  })
_sym_db.RegisterMessage(GateDefinition)

ArgDefinition = _reflection.GeneratedProtocolMessageType('ArgDefinition', (_message.Message,), {
  'DESCRIPTOR' : _ARGDEFINITION,
  '__module__' : 'platforms.google.cirq_google.api.v2.device_pb2'
  # @@protoc_insertion_point(class_scope:cirq_google.api.v2.ArgDefinition)
  })
_sym_db.RegisterMessage(ArgDefinition)

ArgumentRange = _reflection.GeneratedProtocolMessageType('ArgumentRange', (_message.Message,), {
  'DESCRIPTOR' : _ARGUMENTRANGE,
  '__module__' : 'platforms.google.cirq_google.api.v2.device_pb2'
  # @@protoc_insertion_point(class_scope:cirq_google.api.v2.ArgumentRange)
  })
_sym_db.RegisterMessage(ArgumentRange)

TargetSet = _reflection.GeneratedProtocolMessageType('TargetSet', (_message.Message,), {
  'DESCRIPTOR' : _TARGETSET,
  '__module__' : 'platforms.google.cirq_google.api.v2.device_pb2'
  # @@protoc_insertion_point(class_scope:cirq_google.api.v2.TargetSet)
  })
_sym_db.RegisterMessage(TargetSet)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'platforms.google.cirq_google.api.v2.device_pb2'
  # @@protoc_insertion_point(class_scope:cirq_google.api.v2.Target)
  })
_sym_db.RegisterMessage(Target)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
