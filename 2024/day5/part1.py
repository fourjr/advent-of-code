import aoc
import numpy as np


raw_page_ordering_rules, raw_pages_to_produce = aoc.get_input(sep='\n\n')
page_ordering_rules = np.array(list(tuple(map(int, x.split('|'))) for x in raw_page_ordering_rules.split('\n')))
updates = [tuple(map(int, x.split(','))) for x in raw_pages_to_produce.split('\n')]
total = 0

for update in updates:
    # verify against rules
    valid = True
    for n, page in enumerate(update):
        rules_with_page = (page_ordering_rules[np.logical_or(page_ordering_rules[:, 1] == page, page_ordering_rules[:, 0] == page)])
        for rule in rules_with_page:
            if rule[0] == page:
                if rule[1] in update and n > np.argwhere(update == rule[1])[0][0]:
                    valid = False
                    break
        if not valid:
            break
    if valid:
        total += update[len(update) // 2]

print(total)
