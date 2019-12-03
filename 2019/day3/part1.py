with open('input.txt') as f:
    inp = f.read()
wires = [i.split(',') for i in inp.splitlines()]
wire_paths = []

for w in wires:
    wire_paths.append([])
    cursor = [0, 0]  # x, y
    wire_paths[-1].append(tuple(cursor[:]))

    for instruction in w:
        command = instruction[0]
        steps = int(instruction[1:])

        for i in range(steps):
            if command == 'R':
                cursor[0] += 1
            elif command == 'L':
                cursor[0] -= 1
            elif command == 'U':
                cursor[1] -= 1
            elif command == 'D':
                cursor[1] += 1
            wire_paths[-1].append(tuple(cursor[:]))

# there are only 2 wire paths
intersections = set(wire_paths[0]).intersection(wire_paths[1])
intersections.remove((0, 0))  # do not count origin
intersections = [sum(abs(i) for i in x) for x in intersections]
print(min(intersections))
