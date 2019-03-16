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
    def __init__(self, variable: str, productions: [Production]):
        self.variable = variable
        self.productions = productions

    def get_first(self, grammar):
        rule_first_set = set()

        for production in self.productions:
            production_first_set = set()
            all_variables_contains_epsilon = True

            for char in production.chars:
                new_rule = grammar.get_rule_by_variable(char)
                if new_rule:
                    char_first_set = new_rule.get_first(grammar)
                    if Production.EPSILON not in char_first_set:
                        production_first_set = production_first_set.union(char_first_set)
                        all_variables_contains_epsilon = False
                        break
                    else:
                        char_first_set.remove(Production.EPSILON)
                        production_first_set = production_first_set.union(char_first_set)
                else:
                    all_variables_contains_epsilon = False
                    char_first_set = {char}
                    production_first_set = production_first_set.union(char_first_set)
                    break

            rule_first_set = rule_first_set.union(production_first_set)
            if all_variables_contains_epsilon:
                rule_first_set = rule_first_set.union({Production.EPSILON})

        return rule_first_set

    def has_epsilon_production(self):
        for production in self.productions:
            if production.is_epsilon():
                return True

        return False

    @staticmethod
    def from_string(rule: str):
        split_by_colon = rule.split(":")

        start_variable = split_by_colon[0].strip()
        productions = [Production(production_string.strip().split(" "))
                       for production_string in split_by_colon[1].split("|")]

        return Rule(start_variable, productions)

    def __str__(self):
        return "%s : %s" %(self.variable, " | ".join([str(production) for production in self.productions]))

class Grammer():
    def __init__(self, rules, start_variable):
        self.rules = rules
        self.start_variable = start_variable

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

    def get_follow(self):
        follow_dict = dict()

        # Initializing follow_dict
        for rule in self.rules:
            follow_dict[rule.variable] = set()

        follow_dict.get(self.rules[0].variable).update({'$'})

        for rule in self.rules:
            for production in rule.productions:
                for i in range(1, len(production.chars) + 1):
                    last_variable = True
                    char_to_compute_follow = production.chars[i - 1]
                    if char_to_compute_follow not in follow_dict.keys():
                        continue
                    for j in range(i, len(production.chars)):
                        current_follower = production.chars[j]

                        new_rule = self.get_rule_by_variable(current_follower)

                        if new_rule:
                            first = new_rule.get_first(self)
                            if Production.EPSILON in first:
                                first.remove(Production.EPSILON)
                                follow_dict.get(char_to_compute_follow).update(first)
                            else:
                                follow_dict.get(char_to_compute_follow).update(first)
                                last_variable = False
                                break
                        else:
                            follow_dict.get(char_to_compute_follow).update(current_follower)
                            last_variable = False
                            break

                    if last_variable:
                        if char_to_compute_follow in follow_dict.keys():
                            follow_dict.get(char_to_compute_follow).update(follow_dict.get(rule.variable))

        return follow_dict

    @staticmethod
    def from_string(grammar: [str]):
        start_variable = grammar[0].split(" ")[0]
        rules = []

        for line in grammar:
            rules.append(Rule.from_string(line))

        return Grammer(rules, start_variable)

    def get_first_and_follow(self):
        first = self.get_first()
        follow = self.get_follow()

        output_string = ""
        for rule in self.rules:
            variable = rule.variable
            output_string += f"{variable} : {' '.join(first[variable])} : {' '.join(follow[variable])}\n"

        return output_string
    def __str__(self):
        return "\n".join([str(rule) for rule in self.rules])

def solve(file_name: str):
    input_file_path = parse_args()
    input_lines = read_input_file(input_file_path)
    with open(Path(os.getcwd(),
                   file_name).absolute().as_posix(),
              "w") as f:
        f.write(str(Grammer.from_string(input_lines).get_first_and_follow()))

def parse_args():
    parser = argparse.ArgumentParser(add_help=True,
                                     description='Sample Commandline')

    parser.add_argument('--file', action="store",
                        nargs="?", metavar="input_file")

    args = parser.parse_args()

    return args.file

def read_input_file(path: str):
    """Read lines in path"""
    with open(path, "r") as f:
        return f.readlines()


if __name__ == '__main__':
    solve("task_5_result.txt")
