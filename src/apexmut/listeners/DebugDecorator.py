from antlr4 import TerminalNode, ErrorNode, ParserRuleContext
from apexmut.antlr.ApexListener import ApexListener
from apexmut.listeners.ListenerDecoratorBase import ListenerDecoratorBase


class DebugDecorator(ListenerDecoratorBase):

    def __init__(self, listener: ApexListener, debugFile):
        super().__init__(listener)
        self._debugFile = debugFile

    def debugLog(self, value):
        self._debugFile.write(value + '\n')

    def visitTerminal(self, node: TerminalNode):
        self._listener.visitTerminal(node)
        self.debugLog('------TERMINAL: ' + str(type(node)).upper())
        self.debugLog('------------RULE=' + self._listener.lookupRuleName(node.getParent()))
        self.debugLog(str(node))

    def visitErrorNode(self, node: ErrorNode):
        self._listener.visitErrorNode(node)
        self.debugLog('------ERROR    : ' + str(type(node)))
        self.debugLog(str(node))

    def enterEveryRule(self, ctx: ParserRuleContext):
        self._listener.enterEveryRule(ctx)
        self.debugLog('------ENTER RULE: ' + self.lookupRuleName(ctx))
        self.debugLog("------------LT(1)=" + self._parser._input.LT(1).text)
        self.debugLog(str(list(ctx.getChildren())))

    def exitEveryRule(self, ctx: ParserRuleContext):
        self._listener.exitEveryRule(ctx)
        self.debugLog('------EXIT  RULE: ' + self._listener.lookupRuleName(ctx))
        self.debugLog("------------LT(1)=" + self._parser._input.LT(1).text)
        self.debugLog(str(list(ctx.getChildren())))

    def enterExpression(self, ctx: ParserRuleContext):
        self._listener.enterExpression(ctx)
        self.debugLog('XXXXXXENTER EXPRESSION')
        self.debugLog('Token Interval: ' + str(ctx.getSourceInterval()))
        self.debugLog('Context vars: ' + str(ctx.children))
