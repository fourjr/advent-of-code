import aoc


directory = {'files': 0}
inp = aoc.get_input_as(sep='$ ')
prev_dirs = []  # stack
curr_dir = None
for cmd in inp:
    if cmd == '':
        continue

    if cmd.startswith("cd"):
        goto = cmd[2:].strip()
        if goto == '/':
            # home
            curr_dir = directory
        elif goto == "..":
            # back one
            curr_dir = prev_dirs.pop()
        else:
            prev_dirs.append(curr_dir)
            curr_dir = curr_dir[goto]

    elif cmd.startswith("ls"):
        contents = cmd[2:].strip()
        for c_type, c_name in (i.split(' ') for i in contents.splitlines()):
            if c_type == 'dir':
                curr_dir[c_name] = {'files': 0}
            else:
                curr_dir['files'] += int(c_type)


# calculating sizes
shares = {'count': 0}

sizes = {}
def calculate_size(directory):
    total_size = 0
    for k, v in directory.items():
        if k == "files":
            total_size += v
        else:
            total_size += calculate_size(v)

    if total_size < 100000:
        shares['count'] += total_size

    return total_size

calculate_size(directory)
print(shares['count'])
