# apex-mutation-testing
Basic mutation testing for Salesforce Apex classes.

## Setup
Need to have ANTLR installed (both Java and Python3)
If you don't have ANTLR for Python, run `pip install` on the requirements found in the requirements.txt file
Ensure the ANTLR Java `.jar` (`antlr-4.7.2-complete.jar`) is in the project root directory

(Note the versions must match! To set version on pip install, append `==4.7.2` for example)


The `setup.sh` script processes the default Antlr grammar for Apex (found at `https://github.com/antlr/grammars-v4/tree/master/apex`) and then builds an Antlr Lexer and Parser (and other  necessary files) in the `src/antlr` directory.

The rest of this project is primarily creating listeners to attach to the lexer and parser to build specific functionality (i.e., create mutations of the input classes).