import argparse
from antlr4 import *
from testLexer import testLexer
from testListener import testListener
from testParser import testParser
from antlr4.tree.Trees import Trees

def get_token_type(token):
    if token.type == testLexer.INT:
        return "INT"
    elif token.type == testLexer.NEWLINE:
        return "NEWLINE"
    elif token.type == testLexer.OPERATOR:
        return "OPERATOR"
    else:
        return "ERROR UNKNOWN TOKEN"

def main():

    with open(args.file, "r") as file:
        lines = file.read()
    input_stream = InputStream(lines)
    lexer = testLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = testParser(token_stream)

 #   tree = parser.start()
 #   print(Trees.toStringTree(tree,None, parser))

    token = lexer.nextToken()

    while not token.type == Token.EOF:
        print(get_token_type(token), token.text)
        token = lexer.nextToken()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?", metavar="file")

    args = parser.parse_args()

    print(args.file)
	
    main()	