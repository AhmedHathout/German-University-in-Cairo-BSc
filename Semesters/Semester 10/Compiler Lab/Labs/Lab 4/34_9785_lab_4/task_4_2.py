import argparse
import os
from pathlib import Path

class Production():
    def __init__(self, chars: [str]):
        self.chars = chars

        if chars == []:
            self.chars = ["epsilon"]

    def has_common_prefix_with(self, production):
        return self.chars[0] == production.chars[0]

    def __str__(self):
        return " ".join(self.chars) if self.chars != Rule.EPSILON else Rule.EPSILON

class Rule():
    EPSILON = "epsilon"

    def __init__(self, variable: str, productions: [Production]):
        self.variable = variable
        self.productions = productions
        self.dashes = ""

    def replace_productions(self, productions_with_common_factor: [Production]):
        replace = True

        # This means that this production has a common factor with just itself
        if len(productions_with_common_factor) == 1:
            return None

        new_variable = self.get_new_variable()
        replacement_production = Production([productions_with_common_factor[0].chars[0], new_variable])

        i = 0
        while i < len(self.productions):
            production = self.productions[i]

            if production in productions_with_common_factor:
                if replace:
                    self.productions[i] = replacement_production
                    replace = False
                else:
                    self.productions.remove(production)
                    i -= 1

            i += 1

        new_productions = [Production(production.chars[1:]) for production in productions_with_common_factor]

        return Rule(new_variable, new_productions)



    def eliminate_left_factor(self):

        new_rules = []

        i = 0
        while i < len(self.productions):
            left_production = self.productions[i]
            productions_with_common_factor = [left_production]

            j = i + 1
            while j < len(self.productions):
                right_production = self.productions[j]

                if left_production.has_common_prefix_with(right_production):
                    productions_with_common_factor.append(right_production)

                j += 1

            new_rule = self.replace_productions(productions_with_common_factor)

            if new_rule:
                new_rules.append(new_rule)

            i += 1

        return new_rules

    def get_new_variable(self):
        self.dashes += "'"
        return self.variable + self.dashes

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

    def eliminate_left_factor(self):
        i = 0

        while i < len(self.rules):
            rule = self.rules[i]

            new_rules = rule.eliminate_left_factor()
            for new_rule in reversed(new_rules):
                self.rules.insert(i + 1, new_rule)

            i += 1

        return self


    @staticmethod
    def from_string(grammer: [str]):
        start_variable = grammer[0].split(" ")[0]
        rules = []

        for line in grammer:
            rules.append(Rule.from_string(line))

        return Grammer(rules, start_variable)

    def __str__(self):
        return "\n".join([str(rule) for rule in self.rules])

def solve(file_name: str):
    input_file_path = parse_args()
    input_lines = read_input_file(input_file_path)
    with open(Path(os.getcwd(),
                   file_name).absolute().as_posix(),
              "w") as f:
        f.write(str(Grammer.from_string(input_lines).eliminate_left_factor()))

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
    solve("task_4_2_result.txt")
