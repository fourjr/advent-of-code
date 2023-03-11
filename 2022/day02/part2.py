import aoc


# ROCK PAPER SCISSORS
# A vs B - B win
# A vs C - A win
# B vs C - C win

score = 0
for r1, r2 in aoc.get_input_as(lambda x: x.split(' ')):
    # mapped_r2 = 'ABC'['XYZ'.find(r2)]
    if r2 == 'Y':
        mapped_r2 = r1
    else:
        if r1 == 'A':
            if r2 == 'X':
                # lose
                mapped_r2 = 'C'
            else:
                mapped_r2 = 'B'
        elif r1 == 'B':
            if r2 == 'X':
                # lose
                mapped_r2 = 'A'
            else:
                mapped_r2 = 'C'
        elif r1 == 'C':
            if r2 == 'X':
                # lose
                mapped_r2 = 'B'
            else:
                mapped_r2 = 'A'

    score += 'ABC'.find(mapped_r2) + 1

    if r1 == mapped_r2:
        score += 3

    moves = (r1, mapped_r2)
    if 'A' in moves and 'B' in moves:
        if mapped_r2 == 'B':
            score += 6
    elif 'A' in moves and 'C' in moves:
        if mapped_r2 == 'A':
            score += 6
    elif 'B' in moves and "C" in moves:
        if mapped_r2 == 'C':
            score += 6

print(score)
