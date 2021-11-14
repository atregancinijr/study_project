from state import State


class ConcreteStateA(State):

    def handle_request1(self):
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle_request2(self):
        print("ConcreteStateA handles request2.")

class ConcreteStateB(State):

    def handle_request1(self):
        print("ConcreteStateB handles request1.")

    def handle_request2(self):
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())