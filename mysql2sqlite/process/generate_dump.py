import sqlite3

from database.MySQL import MySQL
from read_input import build_attributes, build_fks, build_tuples
from read_input.create_table import Table
from read_input.read_custom_select import get_custom_queries
from read_input.read_script import _read_from_script_file


class Process:
    def __init__(self, context):
        self.host = context.database_host
        self.username = context.database_username
        self.password = context.database_password
        self.dbname = context.database_name

        self.ignored_tables = context.ignored_tables
        self.ignored_inserts = context.ignored_inserts

        self.outputname = context.outputname

        self.custom_select_file = context.custom_select_file
        self.external_script_file = context.external_tables_script

        self._inputdb = None
        self._tables = None
        self._dump = None
        self._inserts = None
        self._creates = None
        self._from_file = None
        self._custom_queries = None

    def exec_dump(self):
        return self._exec_dump()

    def _get_dump(self):
        result = '{}\n\n{}'.format(self.creates, self.inserts)
        self.input_db.close()
        return result

    def _get_formatted_tables(self):
        return '\n'.join([i.get_formatted_create() for i in self.tables]) + '\n' + self.from_file

    def _get_formatted_inserts(self):
        return ''.join([i.get_formatted_insert() for i in self.tables])

    def _exec_dump(self):
        conn = sqlite3.connect(database=self.outputname)
        cursor = conn.cursor()
        cursor.executescript(self.dump)
        conn.close()

    def _get_tables(self):
        return [Table(i, build_attributes(self.input_db.get_attributes(i)),
                      build_fks(self.input_db.get_foreign_keys(i)),
                      build_tuples(self.input_db.get_tuples(i, self._find_custom_query(i))) if i not in self.ignored_inserts else None)
                for i in self.input_db.get_tables_name() if i not in self.ignored_tables]

    def _find_custom_query(self, table):
        try:
            for i in [x for x in self.custom_queries if x['table'].lower() == table.lower()]:
                return i['query']
        except (KeyError, TypeError):
            return None

    @property
    def custom_queries(self):
        if self._custom_queries is not None:
            return self._custom_queries

        self._custom_queries = get_custom_queries(self.custom_select_file)
        return self._custom_queries

    @property
    def from_file(self):
        if self._from_file is not None:
            return self._from_file

        self._from_file = _read_from_script_file(self.external_script_file)
        return self._from_file

    @property
    def inserts(self):
        if self._inserts is not None:
            return self._inserts

        self._inserts = self._get_formatted_inserts()
        return self._inserts

    @property
    def creates(self):
        if self._creates is not None:
            return self._creates

        self._creates = self._get_formatted_tables()
        return self._creates

    @property
    def dump(self):
        if self._dump is not None:
            return self._dump

        self._dump = self._get_dump()
        return self._dump

    @property
    def tables(self):
        if self._tables is not None:
            return self._tables

        self._tables = self._get_tables()
        return self._tables

    @property
    def input_db(self):
        if self._inputdb is not None:
            return self._inputdb

        self._inputdb = MySQL(database=self.dbname, host=self.host, username=self.username, password=self.password)
        return self._inputdb
