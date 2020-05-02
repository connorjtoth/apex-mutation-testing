from antlr4 import *
from apexListener import apexListener

class MyApexListener(apexListener):

    def __init__(self, debugFile, outputFile, parser):
        self.debug = debugFile
        self.output = outputFile
        self._parser = parser
    
    def debugLog(self, value):
        self.debug.write(value + '\n')
    
    def outputValue(self, value):
        self.output.write(value + '\n')

    def lookupRuleName(self, ctx:ParserRuleContext):
        return self._parser.ruleNames[ctx.getRuleIndex()]

    def visitTerminal(self, node:TerminalNode):
        self.debugLog('------TERMINAL: ' + str(type(node)).upper())
        self.debugLog('------------RULE=' + self.lookupRuleName(node.getParent()))
        self.debugLog(str(node))
        self.outputValue(str(node))

    def visitErrorNode(self, node:ErrorNode):
        self.debugLog('------ERROR    : ' + str(type(node)))
        self.debugLog(str(node))

    def enterEveryRule(self, ctx:ParserRuleContext):
        self.debugLog('------ENTER RULE: ' + self.lookupRuleName(ctx))
        self.debugLog("------------LT(1)=" + self._parser._input.LT(1).text)
        self.debugLog(str(list(ctx.getChildren())))

    def exitEveryRule(self, ctx:ParserRuleContext):
        self.debugLog('------EXIT  RULE: ' + self.lookupRuleName(ctx))
        self.debugLog("------------LT(1)=" + self._parser._input.LT(1).text)
        self.debugLog(str(list(ctx.getChildren())))
