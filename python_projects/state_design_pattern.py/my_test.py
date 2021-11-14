from context import Context
from concrete_states import ConcreteStateA, ConcreteStateB

context = Context(ConcreteStateA())
context.request1()
context.request2()