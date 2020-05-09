from antlr4 import *
from .antlr.ApexListener import ApexListener
from .antlr.ApexParser import ApexParser

class Listener(ApexListener):
    def __init__(self, parser: ApexParser):
        self._parser = parser
        self._mutations = []

    def lookupRuleName(self, ctx: ParserRuleContext):
        return self._parser.ruleNames[ctx.getRuleIndex()]
