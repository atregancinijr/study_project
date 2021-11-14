#Simplest and well-known Creational design patterns.
#Singleton provides you with a mechanism to have one, and only one, object of a given type and provides a global point of access. Avoid conflicting requests on the same resource.
class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
if __name__=='__main__':
    s = Singleton()
    print("Object created", s)
    s1 = Singleton()
    print("Object created", s1)

#1. We allow the creation of only one instance of the Singleton class.
#2. If an instance exists, we will serve the same object again.