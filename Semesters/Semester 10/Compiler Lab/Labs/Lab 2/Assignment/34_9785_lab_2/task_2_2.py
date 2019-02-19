from functools import reduce
import argparse
from pathlib import Path
class State():
    def __init__(self, name: str, is_start_state=False, is_final_state=False):
        self.name = name
        self.is_start_state = is_start_state
        self.is_final_state = is_final_state

    def disable_is_start_state(self):
        self.is_start_state = False
        return self

    def disable_is_final_state(self):
        self.is_final_state = False
        return self

    def get_closure(self, transitions, alphabet: str):
        closure = []
        for transition in transitions:
            if transition.outgoing == self and transition.symbol == alphabet:
                if transition.incoming not in closure:
                    closure.append(transition.incoming)

                for state in transition.incoming.get_closure(transitions, " "):
                    if state not in closure:
                        closure.append(state)

        return closure

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.name == other.name

class Transition():
    def __init__(self, outgoing: State, incoming: State, symbol: str):
        self.outgoing= outgoing
        self.incoming = incoming
        self.symbol = symbol

    @staticmethod
    def from_string(transition_string: str, states_dict: {str: State}):
        transition_split = transition_string.split(", ")
        # Splitting with ", " will remove the space that indicates the epsilon transition.
        # This is to add it manually.
        transition_split[1] = " " if transition_split[1] == "" else transition_split[1]
        return Transition(states_dict[transition_split[0]],
                          states_dict[transition_split[2]],
                          transition_split[1])

    def __str__(self):
        return "(%s, %s, %s)" % (str(self.outgoing), str(self.symbol), str(self.incoming))

class NFA():
    def __init__(self, states: [State], alphabets: [str],transitions: [Transition],
                 start_state: State, final_state: State):

        self.states = states
        self.alphabets = alphabets
        self.transitions = transitions
        self.start_state = start_state
        self.final_state = final_state

    def get_state_transitions(self, state: State):
        return [transition for transition in self.transitions if transition.outgoing == state]

    @staticmethod
    def from_string(nfa_representation: [str]):
        states_line = nfa_representation[0].strip()
        alphabets_line = nfa_representation[1].strip()
        start_state_line = nfa_representation[2].strip()
        final_state_line = nfa_representation[3].strip()
        transitions_line = nfa_representation[4].strip()

        # TODO: Should remove 'q's from start/final and state lines?
        state_names = states_line.split(",")
        states_dict = dict()

        for name in state_names:
            name = name.strip(" \n")
            states_dict.update({name: State(name)})

        start_state = final_state = None

        for state in states_dict.values():
            if state.name == start_state_line:
                state.is_start_state = True
                start_state = state
            if state.name == final_state_line:
                state.is_final_state = True
                final_state = state

        alphabets = alphabets_line.split(",")

        transitions_line_split = transitions_line.split("), (")
        transitions_line_split[0] = transitions_line_split[0].replace("(", "")
        transitions_line_split[-1] = transitions_line_split[-1].replace(")", "")

        transitions = [Transition.from_string(transition_string, states_dict)
                       for transition_string in transitions_line_split]

        return NFA(states_dict.values(), alphabets,
                   transitions, start_state, final_state)

    def to_dfa(self):
        dfa_states = []
        dfa_start_state = DFAState(self.start_state.get_closure(self.transitions, " "), True)
        dfa_states.append(dfa_start_state)

        i = 0
        while i < len(dfa_states):
            dfa_state = dfa_states[i]
            for alphabet in self.alphabets:
                new_dfa_state = dfa_state.get_closure(self.transitions, alphabet)
                for state in dfa_states:
                    # This seems strange but it is because we want to have the same reference
                    if new_dfa_state == state:
                        new_dfa_state = state
                transition = DFATransition(dfa_state, alphabet, new_dfa_state)
                dfa_state.add_dfa_transition(transition)

                if new_dfa_state not in dfa_states:
                    dfa_states.append(new_dfa_state)

            i += 1
        return DFA(dfa_states, self.alphabets)


class DFATransition():
    def __init__(self, outgoing, symbol, incoming):
        self.outgoing = outgoing
        self.symbol = symbol
        self.incoming = incoming

    def __str__(self):
        return "(%s, %s, %s)" % (self.outgoing.name, self.symbol, self.incoming.name)

    def __eq__(self, other):
        return self.outgoing == other.outgoing and \
               self.symbol == other.symbol and \
               self.incoming == other.incoming

class DFAState():
    def __init__(self, nfa_states: [State], is_start_state=False):
        self.nfa_states = nfa_states
        self.is_start_state = is_start_state
        self.name = None
        self.transitions = []


    def add_dfa_transition(self, dfa_transition):
        if dfa_transition not in self.transitions:
            self.transitions.append(dfa_transition)

    # def add_state(self, state: State):
    #     self.nfa_states.add(state)

    def get_closure(self, transitions, alphabet):
        closure = []
        for state in self.nfa_states:
            sub_closure = state.get_closure(transitions, alphabet)
            for state_in_sub_closure in sub_closure:
                if state_in_sub_closure not in closure:
                    closure.append(state_in_sub_closure)
        if not closure:
            return DFAState([State("DEAD")])

        return DFAState(closure)

    def is_final_state(self):
        return True if True in map(lambda s: s.is_final_state, self.nfa_states) else False
        # return reduce(lambda s1, s2: s1.is_final_state or s2.is_final_state, self.nfa_states)

    def __eq__(self, other):
        return self.nfa_states == other.nfa_states

    def __str__(self):
        return self.name

class DFA():
    def __init__(self, dfa_states: [DFAState], alphabets: [str]):
        self.dfa_states = DFA.set_states_names(dfa_states)
        self.alphabets = alphabets
        self.start_state = list(filter(lambda s: s.is_start_state, self.dfa_states))[0]
        self.final_states = [dfa_state for dfa_state in dfa_states if dfa_state.is_final_state()]

    def __str__(self):
        dfa_states = ", ".join([str(dfa_state) for dfa_state in self.dfa_states])
        alphabets = ", ".join(self.alphabets)
        final_states = ", ".join([str(final_state) for final_state in self.final_states])

        transitions = ""
        for dfa_state in self.dfa_states:
            transitions += ", ".join([str(transition) for transition in dfa_state.transitions]) + ","

        transitions = transitions[:-1]

        return "%s\n%s\n%s\n%s\n%s\n" % (dfa_states, alphabets, self.start_state, final_states, transitions)


    @staticmethod
    def set_states_names(dfa_states: [DFAState]):
        current_char = "A"
        for dfa_state in dfa_states:
            dfa_state.name = current_char
            current_char = chr(ord(current_char) + 1)

        return dfa_states

def solve():
    input_file_path = parse_args()
    input_lines = read_input_file(input_file_path)
    output_file_path = get_output_file_path(input_file_path)
    with open(output_file_path, "w") as output_file:
        output_file.write(str(NFA.from_string(input_lines).to_dfa()))

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

if __name__ == '__main__':
    solve()