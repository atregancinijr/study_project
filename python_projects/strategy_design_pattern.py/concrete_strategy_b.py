from strategy import Strategy


class ConcreteStrategyB(Strategy):

    def do_algorithm(self, a_list):
        return reversed(sorted(a_list))
