from antlr4 import ParserRuleContext, TerminalNode
from apexmut.listeners.Listener import Listener
from apexmut.listeners.ListenerDecoratorBase import ListenerDecoratorBase


class IncrementMutator(ListenerDecoratorBase):
    REPLACEMENT_MAP = {
        '++': '--',
        '--': '++'
    }

    def __init__(self, listener: Listener):
        super().__init__(listener)

    # Target rule
    # expression :
    #   | expression ('++' | '--')
    #   | ('+' | '-' | '++' | '--') expression
    def enterExpression(self, ctx: ParserRuleContext):
        self._listener.enterExpression(ctx)

        if ctx.getChildCount() == 2:
            symbol = None
            if isinstance(ctx.getChild(0), TerminalNode):
                symbol = ctx.getChild(0).symbol
            elif isinstance(ctx.getChild(1), TerminalNode):
                symbol = ctx.getChild(1).symbol

            if symbol is not None and symbol.text in self.REPLACEMENT_MAP:
                print()
                print('Context vars: ' + str(ctx.children))
                print(symbol.text)
                print(symbol.start, symbol.stop)
                print(symbol)
                self._listener._mutations.append((self.__class__, symbol, self.REPLACEMENT_MAP[symbol.text]))
