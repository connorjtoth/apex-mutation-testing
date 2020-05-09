import sys
import os.path
'''
Takes input grammar file, outputs same grammar file with name "Apex.g4" in the same
directory as input.
'''


def main(argv):

    if len(argv) != 2:
        raise Exception('An input grammar file must be specified!')

    inputFileDir, inputFileName = os.path.split(argv[1])

    # TODO: Use a grammar to parse the grammar and fix it
    with open(os.path.join(inputFileDir, inputFileName), 'r') as inputFile:
        with open(os.path.join(inputFileDir, 'Apex.g4'), 'w') as outputFile:
            for line in inputFile.readlines():
                line = line.replace(' -> skip', ' -> channel(HIDDEN)')
                line = line.replace('grammar apex;', 'grammar Apex;')
                outputFile.writelines(line)


if __name__ == '__main__':
    main(sys.argv)
