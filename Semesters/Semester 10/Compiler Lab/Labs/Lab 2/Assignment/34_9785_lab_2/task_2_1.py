import argparse
from antlr4 import *
from task_2_1Lexer import task_2_1Lexer
from task_2_1Listener import task_2_1Listener
from task_2_1Parser import task_2_1Parser
from antlr4.tree.Trees import Trees

from pathlib import Path
def get_token_type(token):
    if token.type == task_2_1Lexer.COMMAND:
        return "COMMAND"
    elif token.type == task_2_1Lexer.REG:
        return "REG"
    elif token.type == task_2_1Lexer.IMMEDIATE:
        return "IMMEDIATE"
    elif token.type == task_2_1Lexer.MEMORY:
        return "MEMORY"

def solve(pattern: str):
    input_file_path = parse_args()
    input_lines = read_input_file(input_file_path)
    output_file_path = get_output_file_path(input_file_path)
    with open (output_file_path, "w") as output_file:
        for line in input_lines:
            m = re.finditer(pattern, line)
            for match in m:
                output_file.write(match.group(1) + '_new\n')

def parse_args():
    parser = argparse.ArgumentParser(add_help=True,
                                     description='Sample Commandline')

    parser.add_argument('--file', action="store",
                        help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()
    return args.file

def read_input_file(path: str):
    """Read lines in path"""
    with open(path, "r") as f:
        return f.readlines()

def get_output_file_path(input_file_name: str):
    """append '_result' to the input file name"""
    input_path = Path(input_file_name)
    return Path(input_path.parent, input_path.stem + "_result").with_suffix(input_path.suffix).absolute().as_posix()


def main():
    with open(args.file, "r") as file:
        lines = file.read()
    input_stream = InputStream(lines)
    lexer = task_2_1Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = task_2_1Parser(token_stream)

    #   tree = parser.start()
    #   print(Trees.toStringTree(tree,None, parser))

    token = lexer.nextToken()

    output_file_path = get_output_file_path(args.file)
    with open(output_file_path, "w") as f:
        while not token.type == Token.EOF:
            if get_token_type(token):
                f.write(get_token_type(token) + " " + token.text + "\n")
            token = lexer.nextToken()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True,
                                     description='Sample Commandline')

    parser.add_argument('--file', action="store",
                        help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    main()