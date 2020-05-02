import sys
from antlr4 import *
from apexLexer import apexLexer
from apexParser import apexParser
from myApexListener import MyApexListener



def main(argv):

    if len(argv) != 2:
        raise Exception('An input file must be specified!')

    inputFileName = argv[1]

    inputFileStream = FileStream(inputFileName)
    lexer = apexLexer(inputFileStream)
    tokenStream = CommonTokenStream(lexer)
    parser = apexParser(tokenStream)
    tree = parser.compilationUnit()
    walker = ParseTreeWalker()

    with open('output.txt', 'w') as outputFile, open('debug.txt', 'w') as debugFile:
        listener = MyApexListener(debugFile, outputFile, parser)
        walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
