import aoc

print(max(aoc.get_input_as(lambda x: sum(map(int, x.splitlines())), sep='\n\n')))
