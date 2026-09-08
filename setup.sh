#!/bin/sh
py src/ProcessGrammar.py grammar/original-apex.g4
java -cp ./antlr-4.7.2-complete.jar org.antlr.v4.Tool -o ./src/antlr -Dlanguage=Python3 grammar/Apex.g4