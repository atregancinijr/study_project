##args and ##kwargs. Some function definitions contains the two arguments. Ex: def func(x, y *args, **kwargs);

def func(values):
    for x in values:
        print(x, end=' ')


def func2(*values):          #*args  -> put the result into a list
    for x in values:
        print(x, end=' ')

def func3(**values):         #**kwargs  -> creates a dicitionary
    for x in values:
        print(f'{x}:{values[x]}')

class Func:
    def __init__(self, **kwargs):
        self.values = kwargs

    def func4(self):
        for x in self.values:
            print(f'{x}:{self.values[x]}', end=' ')

if __name__ == '__main__':
    func([1, 2, 3])
    print('\n------------------------------------------------------')
    func2([1, 2, 3])
    print('\n------------------------------------------------------')
    func3(x=1, y=2, z=3)
    print('\n------------------------------------------------------')
    Func4 = Func(x=1, y=2, z=3)
    Func4.func4()


