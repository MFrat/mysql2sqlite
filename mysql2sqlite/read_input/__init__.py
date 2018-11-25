from read_input.create_attribute import Attribute
from read_input.create_table import ForeignKey
from read_input.create_tuple import Tuple


def _file_to_string(filename):
    with open(filename, 'r') as f:
        return ''.join(f.readlines())


def _build_attribute(attr_tuple):
    return Attribute(*attr_tuple)


def _build_fk(attr_tuple):
    return ForeignKey(*attr_tuple)


def _build_tuple(t):
    return Tuple(t)


def _build_attribute_llist(attr_list):
    return [_build_attribute(i) for i in attr_list]


def _build_tuple_list(tuple_list):
    return [_build_tuple(i) for i in tuple_list]


def _build_fk_list(attr_list):
    return [_build_fk(i) for i in attr_list]


def build_attributes(attr_list):
    return _build_attribute_llist(attr_list)


def build_fks(attr_list):
    return _build_fk_list(attr_list)


def build_tuples(tuples_list):
    return _build_tuple_list(tuples_list)
