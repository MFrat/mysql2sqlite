import datetime


def _map(value):
    if value is None:
        return 'null'

    if type(value) is datetime.timedelta:
        return "'{}'".format(str(value))

    if type(value) is datetime.datetime:
        return int(value.timestamp())

    if type(value) is not int:
        return "'{}'".format(str(value))

    return value


class Tuple:
    def __init__(self, tuple):
        self.tuple = tuple

    def _get_formatted(self):
        return '(' + ', '.join([str(_map(i)) for i in self.tuple]) + ')'

    def __str__(self):
        return self._get_formatted()
