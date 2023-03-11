import aoc

print(sum(sorted(aoc.get_input_as(lambda x: sum(map(int, x.splitlines())), sep='\n\n'), reverse=True)[:3]))
