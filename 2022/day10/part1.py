from collections import defaultdict
import aoc
import operator

inp = aoc.get_input_as()
register = {
    'X': 1
}

queue = defaultdict(list)
inp += ['noop'] * 2

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
        if cycle in (20, 60, 100, 140, 180, 220):
            ss_sum += cycle * register['X']
        wait -= 1
        cycle += 1

    action()

print(ss_sum)
