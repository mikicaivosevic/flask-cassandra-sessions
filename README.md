# Server side sessions with Apache Cassandra

The following code implements a session backend using Apache Cassandra. 


## Installation

`pip install cassandra_flask_sessions`

## Configuring the database

To create the table in the Cassandra database, you need the execute the following CQL commands:

```
USE tests;

DROP TABLE IF EXISTS sessions;

CREATE TABLE IF NOT EXISTS sessions (
   sid text,
   data text,
   PRIMARY KEY(sid)
) WITH GC_GRACE_SECONDS = 1;
```

## Usage

```python
from flask import Flask
from cassandra_flask_sessions import CassandraSessionInterface

app = Flask(__name__)
app.session_interface = CassandraSessionInterface(keyspace='tests')
# change session lifetime if you need
# app.config.update({'PERMANENT_SESSION_LIFETIME': 86400})
```

