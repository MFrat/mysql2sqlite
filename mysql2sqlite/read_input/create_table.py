
class Table:
    def __init__(self, name, attributes, fks, tuples):
        self.name = name
        self.attributes = attributes
        self.fks = fks
        self.tuples = tuples

    def get_formatted_create(self):
        return self._get_formatted_create()

    def get_formatted_insert(self):
        return self._get_formatted_insert()

    def _get_formatted_create(self):
        return 'CREATE TABLE {} (\n{}\n);'\
            .format(self.name, self._get_formatted_body())

    def _get_formatted_insert(self):
        if self.tuples is None or len(self.tuples) == 0:
            return ''

        return 'INSERT INTO {table} VALUES {values};\n'\
            .format(table=self.name, values=', '.join([str(i) for i in self.tuples]))

    def _get_formatted_body(self):
        if len(self.fks) == 0:
            return self._format_attributes()

        return ',\n'.join([self._format_attributes(), self._format_fks()])

    def _format_attributes(self):
        return self._format(self.attributes)

    def _format_fks(self):
        return self._format(self.fks)

    def _format(self, array):
        return ',\n'.join(['\t{}'.format(str(i)) for i in array])

    def __str__(self):
        return self._get_formatted_create()


class ForeignKey:
    def __init__(self, this_table, this_attr, other_table, other_attribute, on_update, on_delete):
        self.this_table = this_table
        self.this_attr = this_attr
        self.other_table = other_table
        self.other_attr = other_attribute
        self.on_update = on_update
        self.on_delete = on_delete

    def _get_formatted(self):
        result = 'FOREIGN KEY({this_attr}) REFERENCES {other_table}({other_attr}) {delete} {update}'\
            .format(this_attr=self.this_attr, other_table=self.other_table, other_attr=self.other_attr,
                    delete='ON DELETE {}'.format(self.on_delete) if self.on_delete else '',
                    update='ON UPDATE {}'.format(self.on_update) if self.on_update else '')\
            .strip()

        return result

    def __str__(self):
        return self._get_formatted()
