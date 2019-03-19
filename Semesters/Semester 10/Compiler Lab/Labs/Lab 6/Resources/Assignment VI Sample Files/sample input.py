import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--grammar', action="store", help="path of file to take as input to read grammar", nargs="?", metavar="dfa_file")
    parser.add_argument('--input', action="store", help="path of file to take as input to test strings on LL table", nargs="?", metavar="input_file")
    
    args = parser.parse_args()

    print(args.grammar)
    print(args.input)

