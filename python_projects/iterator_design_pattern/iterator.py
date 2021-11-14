from collections.abc import Iterator


class AlphabeticalOrderIterator(Iterator):

    _position = None
    _reverse = False

    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class CollunmIterator(Iterator):

    def __init__(self, matrix):
        self._matrix = matrix
        self._col = 0
        self._lin = 0

    def __next__(self):
        try:
            value = self._matrix[self._col][self._lin]
            self._col += 1
        except IndexError:
            try:
                self._col = 0
                self._lin += 1
                value = self._matrix[self._col][self._lin]
                self.__next__()
            except IndexError:
                raise StopIteration()

        return value


