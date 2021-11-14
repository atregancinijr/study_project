'''# Singleton design pattern says that there should be one and only one object
of a class.  However, typically what a programmer needs is to have instances sharing the same state. He suggests that developersdevelopers should be bothered about the state and behavior rather than the identity.
 As the concept is based on all objects sharing the same state, it is also known as the Monostate pattern'''
#first way to implement the Borg patter:
class Borg:
    __share__state = {"y" : "2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__share__state
        pass

#Another way to implement the Borg pattern is by tweaking the __new__ method itself. As
#we know, the __new__ method is responsible for the creation of the object instance:
class Borg2:
    __shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg2, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

if __name__ == '__main__': #running as an independent program
    b = Borg()
    b1 = Borg()
    print('1) Borg starting.....\n')
    print("Borg Object 'b': ", b) ## b and b1 are distinct objects
    print("Borg Object 'b1': ", b1)
    print("Object State 'b':", b.__dict__)## b and b1 share same state
    print("Object State 'b1':", b1.__dict__)

    print("\nsetting x from one to four...\n")
    b.x = 4

    print("Borg Object 'b': ", b)  ## b and b1 are distinct objects
    print("Borg Object 'b1': ", b1)
    print("Object State 'b':", b.__dict__)  ## b and b1 share same state
    print("Object State 'b1':", b1.__dict__)
    print('\n')

    #Python uses __dict__ to store the state of every object of a class
    #when we create two instances, 'b' and 'b1', we get two different objects unlike Singleton where we have just one object.
    #However, the object states, b.__dict__ and b1.__dict__ are the same.
    #even if the object variable x changes for object b, the change is copied over to the __dict__ variable that is shared by all objects and even b1 gets this change of the x setting from one to four

if __name__ == '__main__':
    b = Borg2()
    b1 = Borg2()
    print('2) Borg2 starting.....\n')
    print("Borg2 Object 'b': ", b)  ## b and b1 are distinct objects
    print("Borg2 Object 'b1': ", b1)
    print("Object State 'b':", b.__dict__)  ## b and b1 share same state
    print("Object State 'b1':", b1.__dict__)

    print("\nsetting z to four...\n")

    b.z = 4

    print("Borg2 Object 'b': ", b)  ## b and b1 are distinct objects
    print("Borg2 Object 'b1': ", b1)
    print("Object State 'b':", b.__dict__)  ## b and b1 share same state
    print("Object State 'b1':", b1.__dict__)


