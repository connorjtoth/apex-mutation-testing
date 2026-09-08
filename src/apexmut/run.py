import os
import os.path
import time

import antlr4
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from antlr4 import Token, ParserRuleContext

from apexmut.antlr.ApexLexer import ApexLexer
from apexmut.antlr.ApexParser import ApexParser
from apexmut.listeners.BoundaryConditionMutator import BoundaryConditionMutator
from apexmut.listeners.NullReturnMutator import NullReturnMutator
from apexmut.listeners.IncrementMutator import IncrementMutator
from apexmut.listeners.DebugDecorator import DebugDecorator
from apexmut.listeners.OutputDecorator import OutputDecorator
from apexmut.listeners.Listener import Listener

ROOT_OUTPUT_DIR = 'output'


def run(argv):

    if len(argv) != 2:
        raise Exception('An input file must be specified!')

    inputFileName = argv[1]

    outputDirForRunName = ROOT_OUTPUT_DIR + '/run_at_' + str(int(time.time()))
    if not os.path.isdir(ROOT_OUTPUT_DIR):
        os.mkdir(ROOT_OUTPUT_DIR)
    os.mkdir(outputDirForRunName)

    inputFileStream = antlr4.FileStream(inputFileName)
    lexer = ApexLexer(inputFileStream)
    tokenStream = antlr4.CommonTokenStream(lexer)
    parser = ApexParser(tokenStream)
    tree = parser.compilationUnit()
    walker = antlr4.ParseTreeWalker()

    outputFilePath = outputDirForRunName + '/output.txt'
    debugFilePath = outputDirForRunName + '/debug.txt'
    with open(outputFilePath, 'w') as outputFile, open(debugFilePath, 'w') as debugFile:
        listener = Listener(parser)
        listener = OutputDecorator(listener, outputFile)
        listener = DebugDecorator(listener, debugFile)
        listener = BoundaryConditionMutator(listener)
        listener = IncrementMutator(listener)
        listener = NullReturnMutator(listener)
        walker.walk(listener, tree)

    # begin running mutations
    rewriter = TokenStreamRewriter(tokenStream)
        for i, mutation in enumerate(listener._mutations):
            mutatingClass, inputTokenOrContext, replacementText = mutation
            inputText, inputIndex, startIndex, stopIndex = None, None, None, None

            if isinstance(inputTokenOrContext, Token): 
                inputIndex = inputTokenOrContext.tokenIndex
                inputText = inputTokenOrContext.text
                startIndex = inputTokenOrContext.tokenIndex
                stopIndex = inputTokenOrContext.tokenIndex
            elif isinstance(inputTokenOrContext, ParserRuleContext):
                inputIndex = inputTokenOrContext.getRuleIndex()
                inputText = inputTokenOrContext.getText()
                startIndex = inputTokenOrContext.start.tokenIndex
                stopIndex = inputTokenOrContext.stop.tokenIndex

            inputToken = inputTokenOrContext
            print(i, ':', mutatingClass.__name__, 'mutating', inputText, 'to', replacementText)
            print(inputIndex)
            rewriter.replace('mutation_' + str(i) + '_' + mutatingClass.__name__, startIndex, stopIndex, replacementText)

        streamLength = len(tokenStream.tokens)
        for program in rewriter.programs:
            with open(outputDirForRunName + '/' + program + '.txt', 'w') as out:
                out.write(rewriter.getText(program, 0, streamLength))
