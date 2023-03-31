from collections import defaultdict
from dataclasses import dataclass
import re
import operator
import math


import aoc


inp = aoc.get_input_as(sep='\n\n')
class Monkey:
    def __init__(self, items, operation, test_div, true_monkey, false_monkey):
        self.items = items
        self.operate = self._generate_operation(operation)
        self.test = self._generate_test(test_div, true_monkey, false_monkey)

    def _generate_operation(self, operation):
        """Returns function that takes a worry level and returns the new worry level"""
        operation = operation[9:].strip()
        sign, number = operation.split(' ')

        if sign == '*':
            func = operator.mul
        elif sign == '+':
            func = operator.add
        elif sign == '-':
            func = operator.sub

        def operation(x):
            if number == 'old':
                return func(x, x)
            else:
                return func(x, int(number))

        return operation

    def _generate_test(self, test_div, true_monkey, false_monkey):
        def test(worry_level):
            if worry_level % test_div == 0:
                return true_monkey
            return false_monkey

        return test

    def __repr__(self):
        return f'Monkey({self.items})'

@dataclass
class Item:
    worry_level: int

monkeys = []


test_divs = []
for text in inp:
    matches = re.findall(
        r'Monkey \d:\n  Starting items: ([\d, ]+)\n  '
        r'Operation: (new = old [\+\-\*] (?:[\d]+|(?:old)))\n  '
        r'Test: divisible by (\d+)\n    '
        r'If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)+',
        text, re.MULTILINE
    )

    for items, operation, test_div, true_monkey, false_monkey in matches:
        monkeys.append(Monkey(
            list(map(Item, map(int, items.split(', ')))),
            operation, int(test_div), int(true_monkey), int(false_monkey)
        ))
        test_divs.append(int(test_div))

lcm_tests = math.lcm(*test_divs)


inspect_count = defaultdict(int)

for _ in range(10000):
    for monkey_n, monkey in enumerate(monkeys):
        for item in monkey.items[:]:
            inspect_count[monkey_n] += 1
            item.worry_level = monkey.operate(item.worry_level) % lcm_tests

            pass_to = monkey.test(item.worry_level)
            monkey.items.remove(item)
            monkeys[pass_to].items.append(item)  

print(operator.mul(*sorted(inspect_count.values())[-2:]))
