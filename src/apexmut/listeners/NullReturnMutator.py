from antlr4 import ParserRuleContext, TerminalNode
from apexmut.listeners.Listener import Listener
from apexmut.listeners.ListenerDecoratorBase import ListenerDecoratorBase


class NullReturnMutator(ListenerDecoratorBase):

    def __init__(self, listener: Listener):
        super().__init__(listener)

    # Target rule
    # statement: RETURN expression? ';'
    def enterStatement(self, ctx: ParserRuleContext):
        self._listener.enterStatement(ctx)

        if isinstance(ctx.getChild(0), TerminalNode) and ctx.getChild(0).symbol.text == 'return':           
            expression = ctx.getChild(1)
            if expression.getText() != ';':
                if (not expression.getChildCount() == 1) or (not isinstance(expression.getChild(0), TerminalNode)) or expression.getChild(0).symbol.text != 'null':
                    print()
                    print('Context vars: ' + str(ctx.children))
                    print(expression.getText())
                    print(expression.start, expression.stop)
                    print(expression)
                    self._listener._mutations.append((self.__class__, expression, 'NULL'))

            print('STATEMENT: ' + str(expression))

            # TODO: Issue because context of an expression is different than a terminal (e.g., '++'), so need to actually do research to figure this out.