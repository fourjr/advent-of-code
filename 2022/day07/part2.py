import aoc


inp = aoc.get_input_as(sep='$ ')
prev_dirs = []  # stack
directory = {'files': 0}
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
    else:
        raise NotImplementedError("other commands not implemented, only cd/ls")

# calculating sizes
sizes = {}
def calculate_size(directory, name):
    total_size = 0
    for k, v in directory.items():
        if k == "files":
            total_size += v
        else:
            total_size += calculate_size(v, k)

    sizes[name] = total_size
    return total_size


calculate_size(directory, '/')
free_space = 70000000 - sizes['/']
space_required = 30000000 - free_space

print(sorted(filter(lambda x: x >= space_required, sizes.values()))[0])
