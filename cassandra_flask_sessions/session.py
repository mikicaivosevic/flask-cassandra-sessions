import json
from uuid import uuid4

from flask.sessions import SessionInterface, SessionMixin
from werkzeug.datastructures import CallbackDict


class CassandraSession(CallbackDict, SessionMixin):

    def __init__(self, initial=None, sid=None):
        CallbackDict.__init__(self, initial)
        self.sid = sid


class CassandraSessionInterface(SessionInterface):

    def __init__(self, connection_provider, session_cls=CassandraSession):
        """
        :param cassandra_flask_sessions.connection.AbstractConnectionProvider connection_provider:
        """
        self.__session_cls = session_cls
        self.__connection_provider = connection_provider

    def open_session(self, app, request):
        sid = request.cookies.get(app.session_cookie_name)
        if sid:
            connection = self.__connection_provider.get_connection()
            stored_session = connection.execute(
                'SELECT sid, data FROM sessions WHERE sid=%s', [sid]
            ).current_rows

            if stored_session:
                data = None
                if stored_session[0].data is not None:
                    data = json.loads(stored_session[0].data)
                return self.__session_cls(initial=data, sid=stored_session[0].sid)

        return self.__session_cls(sid=str(uuid4()))

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        connection = self.__connection_provider.get_connection()
        if not session:
            connection.execute_async("DELETE FROM sessions WHERE sid=%s", [session.sid])
            response.delete_cookie(app.session_cookie_name, domain=domain)
            return
        cass_exp = app.permanent_session_lifetime
        cookie_exp = self.get_expiration_time(app, session)
        data = json.dumps(dict(session))

        connection.execute_async(
            "INSERT INTO sessions (sid, data) VALUES (%s, %s) USING TTL %s",
            [session.sid, data, int(cass_exp.total_seconds())])

        response.set_cookie(app.session_cookie_name, session.sid,
                            expires=cookie_exp,
                            httponly=True, domain=domain)
