from device import Device


class Radio(Device):

    def __init__(self):
        super().__init__()
        self._volume = 5
        self._channel = 90

    @property
    def device_type(self):
        return 'Radio'

    @property
    def volume(self):
        print(f'Radio Volume is {self._volume}')
        return self._volume

    @volume.setter
    def volume(self, percent):
        self._volume =  percent
        print(f'Setting Radio Volume ...')

    @property
    def channel(self):
        print(f'Radio Channel is {self._channel} MHz')
        return self._channel

    @channel.setter
    def channel(self, channel):
        self._channel = channel
        print(f'Setting Radio Channel ...')


class TV(Device):

    def __init__(self):
        super().__init__()
        self._volume = 10
        self._channel = 2

    @property
    def device_type(self):
        return 'TV'

    @property
    def volume(self):
        print(f'TV Volume is {self._volume}')
        return self._volume

    @volume.setter
    def volume(self, percent):
        self._volume =  percent
        print(f'Setting TV Volume...')

    @property
    def channel(self):
        print(f'TV is channel {self._channel}')
        return self._channel

    @channel.setter
    def channel(self, channel):
        self._channel = channel
        print(f'Setting TV to channel...')
