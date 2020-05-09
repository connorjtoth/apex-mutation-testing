
from antlr4 import *
from antlr4.TokenStreamRewriter import *
from src.antlr.ApexLexer import ApexLexer
from src.antlr.ApexParser import ApexParser
from src.antlr.ApexListener import ApexListener
from src.decorators.OutputDecorator import OutputDecorator
from src.decorators.DebugDecorator import DebugDecorator
from src.decorators.BoundaryConditionMutator import BoundaryConditionMutator
from src.Listener import Listener
import sys
import os
import os.path
import shutil
import datetime
import time
import random

ROOT_OUTPUT_DIR = 'output'


def main(argv):

    if len(argv) != 2:
        raise Exception('An input file must be specified!')

    inputFileName = argv[1]


    outputDirForRunName = ROOT_OUTPUT_DIR + '/run_at_' + str(int(time.time()))
    if not os.path.isdir(ROOT_OUTPUT_DIR):
        os.mkdir(ROOT_OUTPUT_DIR)
    os.mkdir(outputDirForRunName)


    inputFileStream = FileStream(inputFileName)
    lexer = ApexLexer(inputFileStream)
    tokenStream = CommonTokenStream(lexer)
    parser = ApexParser(tokenStream)
    tree = parser.compilationUnit()
    walker = ParseTreeWalker()

    with open(outputDirForRunName + '/output.txt', 'w') as outputFile, open(outputDirForRunName + '/debug.txt', 'w') as debugFile:
        listener = Listener(parser)
        listener = OutputDecorator(listener, outputFile)
        listener = DebugDecorator(listener, debugFile)
        listener = BoundaryConditionMutator(listener)
        walker.walk(listener, tree)
    
    # begin running mutations
    rewriter = TokenStreamRewriter(tokenStream)
    for i, mutation in enumerate(listener._mutations):
        mutatingClass, inputToken, replacementText = mutation
        print(i, ':', mutatingClass.__name__, 'mutating', inputToken.text, 'to', replacementText)
        print(inputToken.tokenIndex)
        rewriter.replace('mutation_' + str(i), inputToken.tokenIndex, inputToken.tokenIndex, replacementText)

    streamLength = len(tokenStream.tokens)
    for program in rewriter.programs:
        with open(outputDirForRunName + '/' + program + '.txt', 'w') as out:
            out.write(rewriter.getText(program, 0, streamLength))

if __name__ == '__main__':
    main(sys.argv)
