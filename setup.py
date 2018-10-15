from distutils.core import setup


setup(
    name='cassandra_flask_sessions',
    packages=['cassandra_flask_sessions'],
    install_requires=['cassandra-driver', 'flask'],
    version='0.6.0',
    description='Server side sessions with Apache Cassandra',
    author='Mikica Ivosevic',
    author_email='mikica.ivosevic@gmail.com',
    url='https://github.com/mikicaivosevic/flask-cassandra-sessions',
    keywords=['flask', 'cassandra', 'sessions'],
    classifiers=[
        'Framework :: Flask',
        'Programming Language :: Python',
    ],
)
