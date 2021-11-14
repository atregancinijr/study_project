# Lazy instantiation makes sure that the object gets created when it’s actually needed.
#it calls the __init__ method but no new object gets created. However, actual object creation happens when we call Singleton.getInstance().
class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('__init__ method called..')
        else:
            print(f'Instance already created: {self.getInstance()}')

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


if __name__ == '__main__':
    s = Singleton()  ## class initialized, but object not created
    print("Object created", Singleton.getInstance()) # Object gets created here
    print('')
    s1 = Singleton() ## instance already created
