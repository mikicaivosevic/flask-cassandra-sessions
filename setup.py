from distutils.core import setup
setup(
  name = 'cassandra_flask_sessions',
  packages = ['cassandra_flask_sessions'], # this must be the same as the name above
  version = '0.1',
  description = 'Server side sessions with Apache Cassandra',
  author = 'Mikica Ivosevic',
  author_email = 'mikica.ivosevic@gmail.com',
  url = 'https://github.com/mikicaivosevic/flask-cassandra-sessions', # use the URL to the github repo
  download_url = 'https://github.com/mikicaivosevic/flask-cassandra-sessions/tarball/0.1', # I'll explain this in a second
  keywords = ['flask', 'cassandra', 'sessions'],
  classifiers = [],
)