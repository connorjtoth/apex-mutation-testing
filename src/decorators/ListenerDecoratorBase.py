from ..Listener import Listener


class ListenerDecoratorBase(Listener):

    def __init__(self, listener: Listener):
        self._listener = listener
        self._parser = listener._parser
        self._mutations = listener._mutations
