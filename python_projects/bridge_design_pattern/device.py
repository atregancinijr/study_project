from abc import ABC, abstractmethod


class Device(ABC):

    def __init__(self):
        self._enable = False

    def is_enable(self):
        return self._enable

    def enable(self):
        print('Turning On...')
        self._enable = True
        return self._enable

    def disable(self):
        print('Turning Off...')
        self._enable = False
        return self._enable

    @property
    @abstractmethod
    def device_type(self):
        pass

    @property
    @abstractmethod
    def volume(self):
        pass

    @volume.setter
    @abstractmethod
    def volume(self, percent):
        pass

    @property
    @abstractmethod
    def channel(self):
        pass

    @channel.setter
    @abstractmethod
    def channel(self, channel):
        pass
