## MySQL2SQLite converter

This project is a Python script that converts a MySQL database into a SQLite one.
It was designed for usage in Android development.
The Script converts Tables and Data, the output is a SQLite database with same Tables
Data.

## Pre-requisites
Python version >= 3.x.x

## Install Requirements
`python -m pip install -U requirements.txt`

## Features
#### Ignore Inserts
You may want ome table's data to not be present in the final SQLite. There is a
env attribute `IGNORED_INSERTS` containing all tables that data will be ignored.

#### Ignore Tables
If you don't want some tables in the SQLite database, you can declare them in a env
attribute called `IGNORED_TABLES`.

#### Outer Tables
It is possible to create some tables that are not present in the MySQL databasse,
to do so, you can use a file containing a script to create those tables you want.

#### Custom Select
For some tables, you can declare a query that will fetch table's data.
The default query is `SELECT * FROM TABLE`
For this, there is a specific attribute `CUSTOM_SELECT_FILE`.

### Environment Attributes
The script uses a .yaml file to store env variables, like database host.

.yaml example:

```yaml
DATABASE_HOST: localhost
DATABASE_PORT: 3306
DATABASE_NAME: mydatabase
DATABASE_USERNAME: root
DATABASE_PASSWORD: root

OUTER_TABLES_SCRIPT: script.sql
CUSTOM_SELECT_FILE: custom_select.txt

SQLITE_OUTPUT_NAME: database.db

IGNORED_TABLES:
  - table1
  - table2

IGNORED_INSERTS:
  - table3
```

##### The first part is the MySQL database connection properties
```yaml
DATABASE_HOST: localhost
DATABASE_PORT: 3306
DATABASE_NAME: mydatabase
DATABASE_USERNAME: root
DATABASE_PASSWORD: root
```

##### Script containing the creation of tables that are not present in MySQL.
```yaml
OUTER_TABLES_SCRIPT: script.sql
```

File example:
```sql
CREATE TABLE table1 (
	a	INTEGER UNIQUE,
	b	INTEGER PRIMARY KEY AUTOINCREMENT,
	c	INTEGER,
	d	INTEGER NOT NULL
);
CREATE TABLE table2 (
	a	INTEGER UNIQUE,
	b	INTEGER PRIMARY KEY AUTOINCREMENT,
	c	INTEGER,
	d	INTEGER NOT NULL
);
```

##### Text file containing custom select query
```yaml
CUSTOM_SELECT_FILE: custom_select.txt
```

File example:

```
table1: SELECT * FROM TABLE1 WHERE attr = "2018.2";
table2: SELECT * FROM TABLE2 WHERE attr = "2018.2";
```

##### Output SQLite database name
```yaml
SQLITE_OUTPUT_NAME: database.db
```

##### List of ignored tables
```yaml
IGNORED_TABLES:
  - table1
  - table2
```

##### List of ignored inserts
```yaml
IGNORED_INSERTS:
  - table3
```

### Run
`python main.py -env (dev|prd)`