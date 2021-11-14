from base_handler import BaseHandler


class ConcreteHandlerA(BaseHandler):

    def handle(self, request):
        if request == 'A':
            print('Handler A: I can handle with this')
        else:
            print(f"Handler A: I can't handle with '{request}'")
            return super().handle(request)


class ConcreteHandlerB(BaseHandler):

    def handle(self, request):
        if request == 'B':
            print('Handler B: I can handle with this')
        else:
            print(f"Handler B: I can't handle with '{request}'")
            return super().handle(request)


class ConcreteHandlerC(BaseHandler):

    def handle(self, request):
        if request == 'C':
            print('Handler C: I can handle with this')
        else:
            print(f"Handler C: I can't handle with '{request}'")
            return super().handle(request)
