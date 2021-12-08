from aoc import get_input_as, submit

inp = get_input_as()

SEGMENTS = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

count = 0
for i in inp:
    patterns, output = i.split(' | ')
    for x in output.split(' '):
        if len(x) in [len(SEGMENTS[h]) for h in (1, 4, 7, 8)]:
            count += 1

submit(count)