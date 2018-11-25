import mysql.connector


def _get_tablename(tablename):
    if tablename is None:
        raise ValueError('Tablename cannot be None')

    return tablename.upper()


class MySQL:
    def __init__(self, host, database, username, password):
        self.host = host
        self.database = database
        self.username = username
        self.password = password

        self._tables_name_query = 'SELECT table_name FROM information_schema.tables where table_schema=\'{}\''\
                                  .format(self.database)
        self._attributes_query = 'DESCRIBE {}'
        self._tuples_query = 'SELECT * FROM {}'
        self._fk_query = "SELECT i.TABLE_NAME, k.COLUMN_NAME, k.REFERENCED_TABLE_NAME, k.REFERENCED_COLUMN_NAME, j.UPDATE_RULE, j.DELETE_RULE " \
                "FROM information_schema.TABLE_CONSTRAINTS i LEFT JOIN information_schema.KEY_COLUMN_USAGE k " \
                "ON i.CONSTRAINT_NAME = k.CONSTRAINT_NAME JOIN information_schema.REFERENTIAL_CONSTRAINTS j " \
                "ON i.CONSTRAINT_NAME = j.CONSTRAINT_NAME " \
                "WHERE i.CONSTRAINT_TYPE = 'FOREIGN KEY' AND i.TABLE_NAME = '{0}';"

        self._conn = None

    def get_tables_name(self):
        return self._get_tables_name()

    def get_tuples(self, tablename, custom_query=None):
        return self._get_tuples(tablename, custom_query)

    def get_attributes(self, tablename):
        return self._get_attributes(tablename)

    def get_foreign_keys(self, tablename):
        return self._get_foreign_keys(tablename)

    def _get_foreign_keys(self, tablename):
        tablename = _get_tablename(tablename)
        return self._execute_query(self._fk_query.format(tablename))

    def _get_attributes(self, tablename):
        tablename = _get_tablename(tablename)
        return self._execute_query(self._attributes_query.format(tablename.upper()))

    def _get_tuples(self, tablename, custom_query):
        tablename = _get_tablename(tablename)
        if custom_query is None:
            return self._execute_query(self._tuples_query.format(tablename.upper()))

        return self._execute_query(custom_query)

    def _get_tables_name(self):
        tables = self._execute_query(self._tables_name_query)
        return [i[0] for i in tables]

    def _execute_query(self, query):
        cursor = self.conn.cursor()
        if cursor is None:
            return None

        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def close(self):
        if self._conn is None:
            return

        self._conn.close()
        self._conn = None

    @property
    def conn(self):
        if self._conn is not None:
            return self._conn

        self._conn = mysql.connector.connect(user=self.username, password=self.password,
                                             host=self.host, database=self.database)
        return self._conn
