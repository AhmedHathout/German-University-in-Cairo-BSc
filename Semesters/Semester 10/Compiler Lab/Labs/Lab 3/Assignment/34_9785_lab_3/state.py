class State():
    states_dict = dict()

    def __init__(self, name: str):

        self.name = name
        self.transitions = dict()
        self.expression = ""
        self.action = ""
        self.is_start_state = False
        self.is_final_state = False

    def __str__(self):
        return self.name

    @staticmethod
    def from_strings(states_names: [str], start_state_name: str,
                     final_states_names: [str], transitions: [(str)],
                     states_expressions: [(str)], expressions_actions: [(str)]) -> []:

        for current_state_name in states_names:
            current_state = State(current_state_name)
            State.states_dict[current_state_name] = current_state

        State.states_dict.get(start_state_name).is_start_state = True

        for final_state_name in final_states_names:
            State.states_dict.get(final_state_name).is_final_state = True

        for from_state_name, sybmol, to_state_name in transitions:
            State.states_dict.get(from_state_name).transitions[sybmol] \
                = State.states_dict.get(to_state_name)

        for state_name, expression in states_expressions:
            State.states_dict.get(state_name).expression = expression.replace("\"", "")

        for expression, action in expressions_actions:
            for state in State.states_dict.values():
                if state.expression == expression.replace("\"", ""):
                    state.action = action

        return list(State.states_dict.values())