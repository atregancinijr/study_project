from remote import Remote

class AdvancedRemote(Remote):

    def __init__(self, device):
        super().__init__(device)


    def mute(self):
        self._device.volume = 0
        print(f'{self._device.device_type} is muted. Volume is {self._device.volume}')
