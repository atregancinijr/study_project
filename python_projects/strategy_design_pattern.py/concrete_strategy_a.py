from strategy import Strategy


class ConcreteStrategyA(Strategy):

    def do_algorithm(self, a_list):
        return sorted(a_list)
