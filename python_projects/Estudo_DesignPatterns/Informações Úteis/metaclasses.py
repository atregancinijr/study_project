# A metaclass is a class of a class, which means that the class is an instance of its metaclass
# With metaclasses, programmers get an opportunity to create classes of their own type from the predefined Python classes.
# EXAMPLE:if you have an object, MyClass, you can create a metaclass, MyKls, that redefines
# the behavior of MyClass to the way that you need
class MyInt(type):
    def __call__(cls, *args, **kwds):
        print("***** Here's My int *****", args)
        print("Now do whatever you want with these objects…")
        return type.__call__(cls, *args, **kwds)

class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4,5)

#Python’s special __call__ method gets called when an object needs to be created for an already existing class