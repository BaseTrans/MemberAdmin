import abc


class IRepository(metaclass=abc.ABCMeta):

    """ an interface for data repository """

    @abc.abstractmethod
    def create(self, entity):
        """ add new entity to a repository """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_pkey(self, pkey, entity):
        """ Retrieves entity by its primary key """
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, entity):
        """ Updates an entity to a repository """
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, entity):
        """ Removes existing entity from a repository """
        raise NotImplementedError()
