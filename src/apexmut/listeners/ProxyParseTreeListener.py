from antlr4 import ParseTreeListener, ParserRuleContext, ErrorNode, TerminalNode

'''
This class is derived from the Java version found here: https://github.com/antlr/antlr4/issues/841.

/**
 * Instances of this class allows multiple listeners to receive events
 * while walking the parse tree. For example:
 *
 * <pre>
 * ProxyParseTreeListener proxy = new ProxyParseTreeListener();
 * ParseTreeListener listener1 = ... ;
 * ParseTreeListener listener2 = ... ;
 * proxy.add( listener1 );
 * proxy.add( listener2 );
 * ParseTreeWalker.DEFAULT.walk( proxy, ctx );
 * </pre>
 
'''
class ProxyParseTreeListener(ParseTreeListener):

    '''
    * Creates a new proxy without an empty list of listeners. Add
    * listeners before walking the tree.
    '''
    def __init__(self, listeners = []):
          self._listeners = listeners

    def enterEveryRule(self, ctx: ParserRuleContext):
        for listener in self._listeners:
            listener.enterEveryRule(ctx)
            ctx.enterRule(listener)

    def exitEveryRule(self, ctx: ParserRuleContext):
       for listener in self._listeners:
          ctx.exitRule(listener)
          listener.exitEveryRule(ctx)

    def visitErrorNode(self, node: ErrorNode):
       for listener in self._listeners:
          listener.visitErrorNode(node)

    def visitTerminal(self, node: TerminalNode):
       for listener in self._listeners:
          listener.visitTerminal(node)


    '''
    * Adds the given listener to the list of event notification recipients.
    *
    * @param listener A listener to begin receiving events.
    '''
    def add(self, listener: ParseTreeListener):
       self._listeners.append(listener)

    '''
    * Removes the given listener to the list of event notification recipients.
    *
    * @param listener A listener to stop receiving events.
    * @return false The listener was not registered to receive events.
    '''
    def remove(self, listener):
       self._listeners.remove(listener)

    '''
    * Returns the list of listeners.
    *
    * @return The list of listeners to receive tree walking events.
    '''
    def getListeners(self):
        return self._listeners;