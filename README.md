# Server side sessions with Apache Cassandra

The following code implements a session backend using Apache Cassandra. 


## Configuring the database

To create the table in the Cassandra database, you need the execute the following CQL commands:

```
USE tests;

DROP TABLE IF EXISTS sessions;

CREATE TABLE IF NOT EXISTS sessions (
   sid text,
   data text,
   PRIMARY KEY(sid)
);
```

## Usage

```python
from flask import Flask

app = Flask(__name__)
app.session_interface = CassandraSessionInterface(keyspace='tests')
```

