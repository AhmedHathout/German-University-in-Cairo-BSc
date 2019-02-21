import os

from state import State
from pathlib import Path

import argparse

class FallbackDFA():
    def __init__(self, states: [State]):
        self.states = states
        self.first_state = next(state for state in self.states
                                  if state.is_start_state)
        self.stack = [self.first_state]
        self.left_head = 0
        self.right_head = 0

    def read_input(self, input: str):
        actions_to_return = []
        current_state = self.first_state

        while self.right_head <= len(input):
            if self.left_head == len(input):
                if current_state.is_final_state:
                    actions_to_return.append(
                        (input[self.right_head:self.left_head], current_state.action))
                    return actions_to_return

                else:
                    while not current_state.is_final_state:
                        if not self.stack:
                            actions_to_return.append(
                                (input[self.right_head:self.left_head], current_state.action))
                            return actions_to_return

                        self.left_head -= 1
                        current_state = self.stack.pop()

                    self.left_head += 1
                    actions_to_return.append((input[self.right_head:self.left_head],
                                              current_state.action))

                    self.right_head = self.left_head
                    del self.stack[:]
                    current_state = self.first_state

            current_char = input[self.left_head]

            current_state = current_state.transitions[current_char]
            self.stack.append(current_state)
            self.left_head += 1

    @staticmethod
    def from_string(input_lines: [str]):
        states_names = input_lines[0].strip().split(", ")
        start_state_name = input_lines[2].strip()
        final_states_names = input_lines[3].strip().split(", ")

        transitions = FallbackDFA.parse_tuples(input_lines[4])
        states_expressions = FallbackDFA.parse_tuples(input_lines[5])
        expressions_actions = FallbackDFA.parse_tuples(input_lines[6])

        states = State.from_strings(states_names, start_state_name,
                                    final_states_names, transitions,
                                    states_expressions, expressions_actions)

        return FallbackDFA(states)


    @staticmethod
    def parse_tuples(tuples_line: str):
        tuples_line_split = tuples_line.strip().split("), (")
        tuples_line_split[0] = tuples_line_split[0].replace("(", "")
        tuples_line_split[-1] = tuples_line_split[-1].replace(")", "")

        return [tuple(tuple_content.split(", ")) for tuple_content in tuples_line_split]


def solve():
    dfa_file_path, input_file_path = parse_args()
    dfa_lines = read_input_file(dfa_file_path)
    input_lines = read_input_file(input_file_path)
    with open(Path(os.getcwd(), "task_3_1_result.txt").absolute().as_posix(), "w") as f:
        f.writelines(", ".join(output) + "\n" for output in FallbackDFA.from_string(dfa_lines).read_input(input_lines[0]))

def parse_args():
    parser = argparse.ArgumentParser(add_help=True,
                                     description='Sample Commandline')

    parser.add_argument('--dfa-file', action="store",
                        help="path of file to take as input to construct DFA",
                        nargs="?", metavar="dfa_file")
    parser.add_argument('--input-file', action="store",
                        help="path of file to take as input to test strings in on DFA",
                        nargs="?", metavar="input_file")

    args = parser.parse_args()

    return (args.dfa_file, args.input_file)


def read_input_file(path: str):
    """Read lines in path"""
    with open(path, "r") as f:
        return f.readlines()

def get_output_file_path(input_file_name: str):
    """append '_result' to the input file name"""
    input_path = Path(input_file_name)
    return Path(input_path.parent, input_path.stem + "_result").with_suffix(input_path.suffix).absolute().as_posix()

if __name__ == '__main__':
    solve()