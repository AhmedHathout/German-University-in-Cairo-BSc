import argparse
import os
from pathlib import Path

class Production():
    def __init__(self, chars: [str]):
        self.chars = chars

    def __str__(self):
        return " ".join(self.chars) if self.chars != Rule.EPSILON else Rule.EPSILON

class Rule():
    EPSILON = "epsilon"

    def __init__(self, variable: str, productions: [Production]):
        self.variable = variable
        self.productions = productions

    def get_alphas(self):
        """A sentential form is an alpha if it starts immediately after the left
           recursive variable"""

        alphas = []
        for production in self.productions:
            if production.chars[0] == self.variable:
                alphas.append(production.chars[1:])

        return alphas

    def get_betas(self):
        return [production.chars for production in self.productions
                if production.chars[0] != self.variable]

    def eliminate_immediate_left_recursion(self):
        variable1 = self.variable
        variable2 = self.variable + "'"

        betas = self.get_betas()
        alphas = self.get_alphas()

        if not alphas:
            return None
        for beta in betas:
            beta.append(variable2)

        for alpha in alphas:
            alpha.append(variable2)

        alphas.append(Rule.EPSILON)

        return (Rule(variable1, [Production(beta) for beta in betas]),
                Rule(variable2, [Production(alpha) for alpha in alphas]))

    def replace_productions_with_rule(self, rule):
        new_productions = []

        for production in self.productions:
            if production.chars[0] == rule.variable:
                for rule_production in rule.productions:
                    new_production = Production(rule_production.chars + production.chars[1:])
                    new_productions.append(new_production)
            else:
                new_productions.append(production)

        self.productions = new_productions

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

    def elimnate_left_recursion(self):

        i = 0
        while i < len(self.rules):
            for j in range(i):
                self.rules[i].replace_productions_with_rule(self.rules[j])

            new_rules = self.rules[i].eliminate_immediate_left_recursion()

            if new_rules:
                self.rules[i] = new_rules[0]
                self.rules.insert(i + 1, new_rules[1])

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
        f.write(str(Grammer.from_string(input_lines).elimnate_left_recursion()))

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
    solve("task_4_1_result.txt")