# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ground_control.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ground_control.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14ground_control.proto\"\x1c\n\nmapRequest\x12\x0e\n\x06number\x18\x01 \x01(\t\"9\n\x08mapReply\x12\x0b\n\x03map\x18\x01 \x03(\t\x12\x0f\n\x07rowsNum\x18\x02 \x01(\t\x12\x0f\n\x07\x63olsNum\x18\x03 \x01(\t\"%\n\x0f\x63ommandsRequest\x12\x12\n\ncommandNum\x18\x01 \x01(\x05\"!\n\rcommandsReply\x12\x10\n\x08\x63ommands\x18\x01 \x01(\t\")\n\x10serialNumRequest\x12\x15\n\rroverPosition\x18\x01 \x01(\t\"#\n\x0eserialNumReply\x12\x11\n\tserialNum\x18\x01 \x01(\t2\xa0\x01\n\rGroundControl\x12\"\n\x06getMap\x12\x0b.mapRequest\x1a\t.mapReply\"\x00\x12\x31\n\x0bgetCommands\x12\x10.commandsRequest\x1a\x0e.commandsReply\"\x00\x12\x38\n\x10getMineSerialNum\x12\x11.serialNumRequest\x1a\x0f.serialNumReply\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3'
)




_MAPREQUEST = _descriptor.Descriptor(
  name='mapRequest',
  full_name='mapRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='mapRequest.number', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=24,
  serialized_end=52,
)


_MAPREPLY = _descriptor.Descriptor(
  name='mapReply',
  full_name='mapReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='map', full_name='mapReply.map', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rowsNum', full_name='mapReply.rowsNum', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='colsNum', full_name='mapReply.colsNum', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=54,
  serialized_end=111,
)


_COMMANDSREQUEST = _descriptor.Descriptor(
  name='commandsRequest',
  full_name='commandsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='commandNum', full_name='commandsRequest.commandNum', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=113,
  serialized_end=150,
)


_COMMANDSREPLY = _descriptor.Descriptor(
  name='commandsReply',
  full_name='commandsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='commands', full_name='commandsReply.commands', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=152,
  serialized_end=185,
)


_SERIALNUMREQUEST = _descriptor.Descriptor(
  name='serialNumRequest',
  full_name='serialNumRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roverPosition', full_name='serialNumRequest.roverPosition', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=187,
  serialized_end=228,
)


_SERIALNUMREPLY = _descriptor.Descriptor(
  name='serialNumReply',
  full_name='serialNumReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialNum', full_name='serialNumReply.serialNum', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=230,
  serialized_end=265,
)

DESCRIPTOR.message_types_by_name['mapRequest'] = _MAPREQUEST
DESCRIPTOR.message_types_by_name['mapReply'] = _MAPREPLY
DESCRIPTOR.message_types_by_name['commandsRequest'] = _COMMANDSREQUEST
DESCRIPTOR.message_types_by_name['commandsReply'] = _COMMANDSREPLY
DESCRIPTOR.message_types_by_name['serialNumRequest'] = _SERIALNUMREQUEST
DESCRIPTOR.message_types_by_name['serialNumReply'] = _SERIALNUMREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

mapRequest = _reflection.GeneratedProtocolMessageType('mapRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAPREQUEST,
  '__module__' : 'ground_control_pb2'
  # @@protoc_insertion_point(class_scope:mapRequest)
  })
_sym_db.RegisterMessage(mapRequest)

mapReply = _reflection.GeneratedProtocolMessageType('mapReply', (_message.Message,), {
  'DESCRIPTOR' : _MAPREPLY,
  '__module__' : 'ground_control_pb2'
  # @@protoc_insertion_point(class_scope:mapReply)
  })
_sym_db.RegisterMessage(mapReply)

commandsRequest = _reflection.GeneratedProtocolMessageType('commandsRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDSREQUEST,
  '__module__' : 'ground_control_pb2'
  # @@protoc_insertion_point(class_scope:commandsRequest)
  })
_sym_db.RegisterMessage(commandsRequest)

commandsReply = _reflection.GeneratedProtocolMessageType('commandsReply', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDSREPLY,
  '__module__' : 'ground_control_pb2'
  # @@protoc_insertion_point(class_scope:commandsReply)
  })
_sym_db.RegisterMessage(commandsReply)

serialNumRequest = _reflection.GeneratedProtocolMessageType('serialNumRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERIALNUMREQUEST,
  '__module__' : 'ground_control_pb2'
  # @@protoc_insertion_point(class_scope:serialNumRequest)
  })
_sym_db.RegisterMessage(serialNumRequest)

serialNumReply = _reflection.GeneratedProtocolMessageType('serialNumReply', (_message.Message,), {
  'DESCRIPTOR' : _SERIALNUMREPLY,
  '__module__' : 'ground_control_pb2'
  # @@protoc_insertion_point(class_scope:serialNumReply)
  })
_sym_db.RegisterMessage(serialNumReply)


DESCRIPTOR._options = None

_GROUNDCONTROL = _descriptor.ServiceDescriptor(
  name='GroundControl',
  full_name='GroundControl',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=268,
  serialized_end=428,
  methods=[
  _descriptor.MethodDescriptor(
    name='getMap',
    full_name='GroundControl.getMap',
    index=0,
    containing_service=None,
    input_type=_MAPREQUEST,
    output_type=_MAPREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getCommands',
    full_name='GroundControl.getCommands',
    index=1,
    containing_service=None,
    input_type=_COMMANDSREQUEST,
    output_type=_COMMANDSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getMineSerialNum',
    full_name='GroundControl.getMineSerialNum',
    index=2,
    containing_service=None,
    input_type=_SERIALNUMREQUEST,
    output_type=_SERIALNUMREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GROUNDCONTROL)

DESCRIPTOR.services_by_name['GroundControl'] = _GROUNDCONTROL

# @@protoc_insertion_point(module_scope)
