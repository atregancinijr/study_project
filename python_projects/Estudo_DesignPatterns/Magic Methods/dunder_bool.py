class MyClass:
    pass


class MyClass2:
    def __bool__(self):
        return False


if __name__ == '__main__':
    print(bool(MyClass()))
    print(bool(MyClass2()))
