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
from cassandra.cluster import Cluster
from cassandra_flask_sessions import AbstractConnectionProvider, CassandraSessionInterface


class ConnectionProvider(AbstractConnectionProvider):

    def __init__(self):
        self.__connection = Cluster(['127.0.0.1']).connect('tests')

    def get_connection(self):
        return self.__connection

app = Flask(__name__)
app.session_interface = CassandraSessionInterface(ConnectionProvider())
# change session lifetime if you need
# app.config.update({'PERMANENT_SESSION_LIFETIME': 86400})
```

You can use custom session class if you need:

```
from flask.sessions import SessionMixin
from werkzeug.datastructures import CallbackDict

class CassandraSession(CallbackDict, SessionMixin):

    def __init__(self, initial=None, sid=None):
        def on_update(self):
            print ('on update')

        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid

app.session_interface = CassandraSessionInterface(ConnectionProvider(), CassandraSession)
```

