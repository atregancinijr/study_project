class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)

#As the metaclass has more control over class creation and object instantiation, it can be used to create Singletons.
#(Note: To control the creation and initialization of a class, metaclasses override the __new__ and __init__ method.)
