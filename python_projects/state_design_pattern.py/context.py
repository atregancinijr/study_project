
class Context:

    _state = None
    """
        A reference to the current state of the Context.
        """
    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        """
                The Context allows changing the State object at runtime.
                """
        print(f'Context: Transition to {type(state).__name__}')
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle_request1()

    def request2(self):
        self._state.handle_request2()
