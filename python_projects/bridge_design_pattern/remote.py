
class Remote:

    def __init__(self, device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enable():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self):
        self._device.volume = self._device.volume - 1


    def volume_up(self):
        self._device.volume = self._device.volume + 1


    def channel_down(self):
        self._device.channel = self._device.channel - 1


    def channel_up(self):
        self._device.channel = self._device.channel + 1
