from receiver import Receiver
from concrete_command import *
from invoker import Invoker

params = 'b', 'a', 'C', 'D'

invoker = Invoker()
receiver = Receiver()

command1 = Command1()

invoker.set_command(command1)
invoker.execute_command()

command2 = Command2(receiver, params)

invoker.set_command(command2)
invoker.execute_command()


