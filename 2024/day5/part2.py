from collections import OrderedDict
from dataclasses import dataclass, field
from typing import List
import aoc
import numpy as np


raw_page_ordering_rules, raw_pages_to_produce = aoc.get_input(sep='\n\n')
page_ordering_rules = np.array(list(tuple(map(int, x.split('|'))) for x in raw_page_ordering_rules.split('\n')))
updates = [tuple(map(int, x.split(','))) for x in raw_pages_to_produce.split('\n')]
total = 0

invalid_updates = []
for update in updates:
    # verify against rules
    valid = True
    rules_that_apply = []
    for n, page in enumerate(update):
        rules_with_page = (page_ordering_rules[np.logical_or(page_ordering_rules[:, 1] == page, page_ordering_rules[:, 0] == page)])
        for rule in rules_with_page:
            if rule[0] == page:
                if rule[1] in update:
                    rules_that_apply.append(rule)
                    if n > np.argwhere(update == rule[1])[0][0]:
                        valid = False
    if not valid:
        invalid_updates.append((update, rules_that_apply))


@dataclass
class Page:
    num: int
    lower: List['Page'] = field(default_factory=list)
    higher: List['Page'] = field(default_factory=list)
    _score: int = None

    def calculate_score(self):
        # prevent recalculating
        if self._score is None:
            self._score = 1 + sum(page.calculate_score() for page in self.lower)
        return self._score


fixed_updates = []
for update, rules in invalid_updates:
    pages_d = OrderedDict()
    for page in update:
        pages_d[page] = Page(page)
    for rule in rules:
        pages_d[rule[0]].higher.append(pages_d[rule[1]])
        pages_d[rule[1]].lower.append(pages_d[rule[0]])

    fixed = sorted(pages_d.keys(), key=lambda x: pages_d[x].calculate_score())
    fixed_updates.append(fixed)

for update in fixed_updates:
    total += update[len(update) // 2]

print(total)
