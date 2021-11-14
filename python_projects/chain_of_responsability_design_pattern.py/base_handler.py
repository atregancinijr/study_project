from handler import Handler


class BaseHandler(Handler):

    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return self._next_handler

    def handle(self, request):
        if self._next_handler is not None:
            self._next_handler.handle(request)
