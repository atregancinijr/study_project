from collections.abc import Iterable
from abc import ABC, abstractmethod
from iterator import AlphabeticalOrderIterator, CollunmIterator


class Collection(ABC):

    @abstractmethod
    def add_item(self, item):
        pass


class WordsCollection(Iterable):

    def __init__(self):

        self._collection = []

    def __iter__(self):
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)


class MatrixCollection(Iterable, Collection):

    def __init__(self):

        self._matrix = []

    def __iter__(self):
        return CollunmIterator(self._matrix)

    def add_item(self, vector):
        self._matrix.append(vector)

    def show(self):
        print(self._matrix)