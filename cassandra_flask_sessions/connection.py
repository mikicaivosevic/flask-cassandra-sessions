import abc


class AbstractConnectionProvider(object):

    @abc.abstractmethod
    def get_connection(self):
        """
        :rtype: cassandra.cluster.Session
        """
        pass
