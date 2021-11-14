from command import Command


class Command1(Command):

    def execute(self):
        print(f'Command1: Executing simple command...')

class Command2(Command):

    def __init__(self, receiver, params):
        self._receiver = receiver
        self._params = params

    def execute(self):
        print('Command2: Executing...')
        print(self._receiver.operation(*reversed(sorted((x.lower() for x in self._params)))))
