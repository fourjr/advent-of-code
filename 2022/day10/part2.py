from collections import defaultdict
import aoc
import operator

inp = aoc.get_input_as()
register = {
    'X': 1
}

queue = defaultdict(list)

ss_sum = 0
cycle = 1
cursor = 0

wait = 0

screen = ''


for line in inp:
    if ' ' in line:
        command, args = line.split(' ')
        args = int(args)
    else:
        command = line
        args = None

    action = lambda: None

    if command == 'noop':
        wait += 1

    if command == 'addx':
        wait += 2
        action = lambda: operator.setitem(register, 'X', register['X'] + args)

    while wait != 0:
        if abs(((cycle - 1) % 40) - register['X']) <= 1:
            # sprite position, left right center
            screen += '#'
        else:
            screen += '.'
        if cycle != 0 and cycle % 40 == 0:
            screen += '\n'

        wait -= 1
        cycle += 1


    action()

print(screen)