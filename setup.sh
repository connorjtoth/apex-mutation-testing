#!/bin/sh
py ProcessGrammar.py grammar/original-apex.g4
java org.antlr.v4.Tool -o ./src/antlr -Dlanguage=Python3 grammar/Apex.g4