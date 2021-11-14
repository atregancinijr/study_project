class MyClass:
    def __init__(self, value):
        self.value = value

    def __int__(self):
        print(f'Converting {self.value} to integer:')
        return int(self.value)

    def __float__(self):
        print(f'Converting {self.value} to float:')
        return float(self.value)

    def __complex__(self):
        print(f'Converting {self.value} to complex:')
        return complex(self.value)

if __name__ == '__main__':
    print(int(MyClass(10.0)))

    print(float(MyClass(10)))

    print(complex(MyClass(10.2)))

