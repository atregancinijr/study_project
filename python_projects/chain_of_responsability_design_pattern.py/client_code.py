from concrete_handlers import ConcreteHandlerA, ConcreteHandlerB, ConcreteHandlerC

requests = ['A', 'B', 'C', 'D']
h1 = ConcreteHandlerA()
h2 = ConcreteHandlerB()
h3 = ConcreteHandlerC()

h1.set_next(h2).set_next(h3)

for request in requests:
    print(f"REQUEST : '{request}'")
    h1.handle(request)
    print()