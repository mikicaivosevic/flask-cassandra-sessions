import json
from time import sleep
from unittest import TestCase

from cassandra.cluster import Cluster
from flask import Flask, session

from cassandra_flask_sessions import CassandraSessionInterface, AbstractConnectionProvider


class ConnectionProvider(AbstractConnectionProvider):

    _connection = Cluster(['127.0.0.1']).connect('tests')

    def get_connection(self):
        return self._connection


_app = Flask(__name__)
_app.session_interface = CassandraSessionInterface(ConnectionProvider())


@_app.route('/set/<name>')
def set_session(name):
    session['name'] = name
    return 'ok'


@_app.route('/get')
def get_session():
    return json.dumps(dict(session))


@_app.route('/delete')
def delete_session():
    session.clear()
    return 'ok'


_app.testing = True
_app.app_context().push()


class TestCassandraSessionInterface(TestCase):

    def test_set_get_delete(self):
        name = 'Mikica'
        with _app.test_client() as client:
            session_data = client.get('/set/%s' % name)
            client.set_cookie('localhost', session_data.headers[2][0], session_data.headers[2][1])

            session_data = client.get('/get')
            self.assertEqual(json.dumps({'name': name}), session_data.data)

            client.get('/delete')

            session_data = client.get('/get')

            self.assertEqual('{}', session_data.data)

    def test_lifetime_interval(self):
        name = 'Mikica'
        session_lifetime = _app.config['PERMANENT_SESSION_LIFETIME']
        _app.config.update({'PERMANENT_SESSION_LIFETIME': 1})
        with _app.test_client() as client:
            session_data = client.get('/set/%s' % name)
            client.set_cookie('localhost', session_data.headers[2][0], session_data.headers[2][1])

            session_data = client.get('/get')
            self.assertEqual(json.dumps({'name': name}), session_data.data)
            sleep(2)

            session_data = client.get('/get')

            self.assertEqual('{}', session_data.data)

        _app.config.update({'PERMANENT_SESSION_LIFETIME': session_lifetime})
