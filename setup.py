from distutils.core import setup
setup(
  name = 'cassandra_flask_sessions',
  packages = ['cassandra_flask_sessions'], # this must be the same as the name above
  install_requires = ['cassandra-driver'],
  version = '0.5',
  description = 'Server side sessions with Apache Cassandra',
  author = 'Mikica Ivosevic',
  author_email = 'mikica.ivosevic@gmail.com',
  url = 'https://github.com/mikicaivosevic/flask-cassandra-sessions', # use the URL to the github repo
  download_url = 'https://github.com/mikicaivosevic/flask-cassandra-sessions/archive/0.3.tar.gz', # I'll explain this in a second
  keywords = ['flask', 'cassandra', 'sessions'],
  classifiers = [],
)
