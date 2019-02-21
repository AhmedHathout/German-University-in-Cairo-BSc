import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--dfa-file', action="store", help="path of file to take as input to construct DFA", nargs="?", metavar="dfa_file")
    parser.add_argument('--input-file', action="store", help="path of file to take as input to test strings in on DFA", nargs="?", metavar="input_file")
    
    args = parser.parse_args()

    print(args.dfa_file)
    print(args.input_file)

