from concrete_strategy_a import ConcreteStrategyA
from concrete_strategy_b import ConcreteStrategyB
from context import Context

''' The client code picks a CONCRETE STRATEGY and PASSES IT TO the CONTEXT.
    The client should be aware of the differences between strategies in order to make the right choice.'''

some_list = ['5', '2', '3', '6', '4', '1']

context = Context(ConcreteStrategyA())
context.do_some_business_logic(some_list)

context = Context(ConcreteStrategyB())
context.do_some_business_logic(some_list)