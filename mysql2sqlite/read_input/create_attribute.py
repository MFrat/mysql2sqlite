import re

MAP_TYPES = {
    'int\(\d+\)': 'INTEGER',
    'smallint\(\d+\)': 'INTEGER',
    'varchar\(\d+\)': 'TEXT',
    'char\(\d+\)': 'TEXT',
    'time': 'TEXT',
    'datetime': 'INTEGER'
}


def _get_mapped_type(type):
    for i in MAP_TYPES:
        reg = re.compile(i)
        if reg.match(type):
            return MAP_TYPES[i]

    return type


class Attribute:
    def __init__(self, name, attr_type, null, key, default, extra):
        self.name = name
        self._attr_type = attr_type
        self._null = null
        self._default = default
        self._key = key
        self._extra = extra

        self._type = None
        self._notnull = None
        self._ispk = None
        self._default_value = None
        self._isunique = None

    @property
    def default_value(self):
        if self._default_value is not None:
            return self._default_value

        if self.type != 'TEXT' or self._default is None:
            self._default_value = self._default
        else:
            self._default_value = '"{}"'.format(self._default)

        return self._default_value

    @property
    def ispk(self):
        if self._ispk is not None:
            return self._ispk

        self._ispk = self._key == 'PRI'
        return self._ispk

    @property
    def isunique(self):
        if self._isunique is not None:
            return self._isunique

        self._isunique = self._key == 'UNI'
        return self._isunique

    @property
    def notnull(self):
        if self._notnull is not None:
            return self._notnull

        self._notnull = self._null == 'NO'
        return self._notnull

    @property
    def type(self):
        if self._type is not None:
            return self._type

        self._type = _get_mapped_type(self._attr_type)
        return self._type

    def get_formatted(self):
        return self._get_formatted()

    def _get_formatted_pk(self):
        return 'PRIMARY KEY' if self.ispk else ''

    def _get_formatted_notnull(self):
        return 'NOT NULL' if self.notnull else ''

    def _get_formatted_unique(self):
        return 'UNIQUE' if self.isunique else ''

    def _get_formatted_default(self):
        return 'DEFAULT {}'.format(self.default_value) if self.default_value is not None else ''

    def _get_formatted(self):
        result = '{name} {type} {nn} {uni} {pk} {default}'\
            .format(name=self.name, type=self.type, pk=self._get_formatted_pk(), nn=self._get_formatted_notnull(),
                    uni=self._get_formatted_unique(), default=self._get_formatted_default()).strip()
        return re.sub('\s{2,}', ' ', result)

    def __str__(self):
        return self._get_formatted()
