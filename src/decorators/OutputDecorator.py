from antlr4 import *
from ..antlr.ApexListener import ApexListener
from ..Listener import Listener
from .ListenerDecoratorBase import ListenerDecoratorBase

class OutputDecorator(ListenerDecoratorBase):

    def __init__(self, listener: Listener, outputFile):
        super().__init__(listener)
        self._output = outputFile

    def outputValue(self, value):
        self._output.write(value + '\n')

    def visitTerminal(self, node: TerminalNode):
        self._listener.visitTerminal(node)
        self.outputValue(str(node))