import re

from read_input import _file_to_string


def get_custom_queries(filename):
    return _parse(_filter(_read_file(filename)))


def _read_file(filename):
    return _file_to_string(filename)


def _filter(string):
    string = re.sub(r'\s{2,}', ' ', string)
    return string.replace('\n', ' ')


def _build_dict(t):
    try:
        return {'table': t[0], 'query': t[1]}
    except IndexError:
        raise IndexError('Error during parsing custom selects: {}'.format(t))


def _parse(string):
    reg = re.compile('\s*(\w+)\s*:(.+?);', re.IGNORECASE)
    result = reg.findall(string)
    return [_build_dict(i) for i in result]