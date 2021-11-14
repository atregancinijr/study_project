from remote import Remote
from concrete_devices import *
from advanced_remote import AdvancedRemote

tv = TV()

remote = AdvancedRemote(tv)
remote.channel_down()
remote.channel_up()
remote.volume_down()
remote.mute()
remote.volume_up()
remote.volume_up()
remote.volume_up()

remote.toggle_power()

radio = Radio()
remote = Remote(radio)
remote.channel_down()
remote.channel_up()
remote.volume_down()
remote.volume_up()
remote.volume_up()
remote.volume_down()

