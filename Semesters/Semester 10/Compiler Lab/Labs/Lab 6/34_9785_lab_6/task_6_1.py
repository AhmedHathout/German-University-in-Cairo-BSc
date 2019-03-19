import argparse
import os
from pathlib import Path

class Production():
    EPSILON = "epsilon"

    def __init__(self, chars: [str]):
        self.chars = chars

        if chars == []:
            self.chars = [Production.EPSILON]

    def get_first(self, grammar):
        first_char = self.chars[0]

        if self.is_epsilon():
            return Production.EPSILON

        rule = grammar.get_rule_by_variable(first_char)
        if rule:
            return rule.get_first(grammar)
        else: # Terminal
            return {first_char}

    def is_epsilon(self):
        return self.chars == [Production.EPSILON]
    def __str__(self):
        return " ".join(self.chars) if self.chars != [Production.EPSILON] else Production.EPSILON

class Rule():
    def __init__(self, variable: str, productions: [Production], first: {str}, follow: {str}):
        self.variable = variable
        self.productions = productions
        self.first = first
        self.follow = follow

    def get_first(self, grammar):
        rule_first_list = []

        for i, production in enumerate(self.productions):
            production_first_set = set()
            all_variables_contains_epsilon = True
            is_recursive = False

            for i, char in enumerate(production.chars):
                if char == self.variable and i == 0:
                    rule_first_list.append(frozenset(self.first))
                    is_recursive = True
                    break
                new_rule = grammar.get_rule_by_variable(char)
                if new_rule:
                    char_first_set = new_rule.get_first(grammar)
                    flat_char_first_set = set()
                    for subset in char_first_set:
                        for entry in subset:
                            flat_char_first_set.add(entry)

                    char_first_set = flat_char_first_set
                    if Production.EPSILON not in char_first_set:
                        production_first_set.update(char_first_set)
                        all_variables_contains_epsilon = False
                        break
                    else:
                        char_first_set.remove(Production.EPSILON)
                        production_first_set.update(char_first_set)
                else:
                    all_variables_contains_epsilon = False
                    char_first_set = {char}
                    production_first_set.update(char_first_set)
                    break

            if is_recursive:
                continue

            rule_first_list.append(frozenset(production_first_set))
            if all_variables_contains_epsilon:
                rule_first_list.append(frozenset({Production.EPSILON}))

        # Check if the algorithm is correct
        for production_firsts in rule_first_list:
            if not production_firsts <= self.first: # checks if subset
                print(rule_first_list)
                print(production_firsts)
                print(self.first)
                raise AssertionError("The computed 'first' set is different than the input")

        return rule_first_list

    @staticmethod
    def from_string(rule: str):
        split_by_colon = rule.split(":")

        start_variable = split_by_colon[0].strip()
        productions = [Production(production_string.strip().split(" "))
                       for production_string in split_by_colon[1].split("|")]
        first = set(split_by_colon[2].strip().split(" "))
        follow = set(split_by_colon[3].strip().split(" "))

        return Rule(start_variable, productions, first, follow)

    def __str__(self):
        return "%s : %s" %(self.variable, " | ".join([str(production) for production in self.productions]))

class Grammar():
    def __init__(self, rules, start_variable):
        self.rules = rules
        self.start_variable = start_variable
        self.variables = {rule.variable for rule in self.rules}
        self.terminals = set()

        for rule in self.rules:
            for production in rule.productions:
                for char in production.chars:
                    if char not in self.variables and not production.is_epsilon():
                        self.terminals.add(char)

    def get_rule_by_variable(self, variable: str):
        for rule in self.rules:
            if rule.variable == variable:
                return rule

        # Redundant
        return None

    def get_first(self):
        first_dict = dict()
        for rule in self.rules:
            first_dict[rule.variable] = rule.get_first(self)
        return first_dict

    @staticmethod
    def from_string(grammar: [str]):
        start_variable = grammar[0].split(" ")[0]
        rules = []

        for line in grammar:
            rules.append(Rule.from_string(line))

        return Grammar(rules, start_variable)

    def __str__(self):
        return "\n".join([str(rule) for rule in self.rules])

class LLTable:
    def __init__(self, grammar):
        self.grammar = grammar
        self.first_dict = grammar.get_first() # {var: {(i, firsts)}}
        self.follow_dict = {rule.variable: rule.follow for rule in grammar.rules}
        self.variables = grammar.variables
        self.terminals = grammar.terminals.union({"$"})

        self.table = self.__fill_table()

    def __fill_table(self):
        table = dict(dict())
        for variable in self.variables:
            table[variable] = dict()
            for terminal in self.terminals:
                table[variable][terminal] = [] # Will be the list of productions

                rule_firsts_list = self.first_dict[variable]
                for i, firsts in enumerate(rule_firsts_list):
                    if terminal in firsts:
                        table[variable][terminal].append(self.grammar.get_rule_by_variable(variable).productions[i])
                    else:
                        if firsts == {Production.EPSILON} and terminal in self.follow_dict[variable]:
                            # This line will just add epsilon
                            table[variable][terminal].append(self.grammar.get_rule_by_variable(variable).productions[i])

        return table

    def __is_variable(self, char):
        return char in self.variables

    def is_LL1_grammar(self):
        for row in self.table.values():
            for cell in row.values():
                if len(cell) > 1:
                    return False

        return True

    def is_string_grammatical(self, input: str):
        stack = []
        stack.append("$")
        stack.append(self.grammar.start_variable)

        current_terminal = ""
        for input_char in input + "$":
            current_terminal += input_char
            if not current_terminal in self.terminals:
                continue
            else:
                while True:
                    char_on_top = stack.pop()
                    if self.__is_variable(char_on_top):
                        productions = self.table[char_on_top][current_terminal]

                        if not productions:
                            return False

                        if not productions[0].is_epsilon():
                            for char in reversed(productions[0].chars):
                                stack.append(char)

                    elif char_on_top == current_terminal:
                        current_terminal = ""
                        break

                    else:
                        return False

        # Probably should just return True since reaching this point means that it is the case
        if not stack:
            return True
        return False

    def __str__(self):
        output = ""
        for variable, terminal_production_dict in self.table.items():
            for terminal, productions in terminal_production_dict.items():
                output += f"{variable} : {terminal} : {str(productions[0]) if productions else ''}\n"

        return output

def solve(table_file_name: str, is_grammatical_file_name: str):
    args = parse_args()
    grammar_file_path, input_file_path = args.grammar, args.input

    grammar_string = read_input_file(grammar_file_path)
    input_to_grammar = read_input_file(input_file_path)

    grammar = Grammar.from_string(grammar_string)
    LL_table = LLTable(grammar)

    if LL_table.is_LL1_grammar():
        table_string = str(LL_table)

        with open(Path(os.getcwd(), table_file_name).absolute().as_posix(),
                  "w") as f:
            f.write(table_string)

        with open(Path(os.getcwd(), is_grammatical_file_name).absolute().as_posix(),
                  "w") as f:
            f.write("yes" if LL_table.is_string_grammatical(input_to_grammar[0]) else "no")

    else:
        with open(Path(os.getcwd(), table_file_name).absolute().as_posix(),
                  "w") as f:
            f.write("invalid LL(1) grammar")

def parse_args():
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--grammar', action="store", help="path of file to take as input to read grammar", nargs="?",
                        metavar="dfa_file")
    parser.add_argument('--input', action="store", help="path of file to take as input to test strings on LL table",
                        nargs="?", metavar="input_file")

    args = parser.parse_args()

    return args

def read_input_file(path: str):
    """Read lines in path"""
    with open(path, "r") as f:
        return f.readlines()


if __name__ == '__main__':
    solve("task_6_1_result.txt", "task_6_2_result.txt")
