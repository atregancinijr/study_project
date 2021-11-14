#The __new__ method actually precedes the __init__ method in the dance of creating an instance of a class.
#__new__ method is responsible for actually creating and returning that instance.
# The __new__ method is the first called and is always static.
class MyClass(object):
    def __new__(cls):
        instance = super(MyClass, cls).__new__(cls)
        print('Só estou fazendo um teste no magic method "__new__" ...')
        return instance
    def __init__(self):
        print('Só estou fazendo um teste no magic method "__init__"...')

if __name__ == '__main__':
    myclass = MyClass()
