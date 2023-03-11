import re

import aoc


drawing, steps_text = aoc.get_input_as(sep='\n\n', no_strip=True)
steps = map(lambda x: map(int, x), re.findall(r"^move (\d+) from (\d+) to (\d+)$", steps_text, flags=re.MULTILINE))

num_stacks = (len(drawing.splitlines()[-1]) + 1) // 4

stacks = []

drawing_lines = drawing.splitlines()[:-1]
for i in range(num_stacks):
    stack = []
    index = i * 4 + 1
    for line in drawing_lines:
        try:
            crate = line[index]
        except IndexError:
            pass
        else:
            if crate != ' ':
                stack.append(crate)

    stacks.append(stack)

for move_count, from_pos, to_pos in steps:
    for i in range(move_count):
        item = stacks[from_pos - 1].pop(0)
        stacks[to_pos - 1].insert(0, item)

for s in stacks:
    print(s[0], end='')