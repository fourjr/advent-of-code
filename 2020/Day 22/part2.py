
with open('input.txt') as f:
    data = f.read()

pl1, pl2 = [i for i in data.split('\n\n')]
pl1 = [int(x) for x in pl1.splitlines()[1:]]
pl2 = [int(x) for x in pl2.splitlines()[1:]]


def play(p1, p2):
    card_formations = set()
    while len(p1) > 0 and len(p2) > 0:
        if (tuple(p1), tuple(p2)) in card_formations:
            return 'p1', p1, p2
        else:
            card_formations.add((tuple(p1), tuple(p2)))
            play1 = p1.pop(0)
            play2 = p2.pop(0)
            if len(p1) >= play1 and len(p2) >= play2:
                winner, _, _ = play(p1[:play1], p2[:play2])
            else:
                if play2 >= play1:
                    winner = 'p2'
                elif play1 > play2:
                    winner = 'p1'
                else:
                    print('error1', play1, play2)

        if winner == 'p1':
            p1.append(play1)
            p1.append(play2)
        elif winner == 'p2':
            p2.append(play2)
            p2.append(play1)
        else:
            print('error', play1, play2)


    if len(p1) > 0:
        winner = 'p1'
    else:
        winner = 'p2'
    return winner, p1, p2

winner, pl1, pl2 = play(pl1, pl2)
score = 0
if winner == 'p1':
    winner = pl1
else:
    winner = pl2
for n, i in enumerate(winner):
    score += i * (len(winner) - n)

print(score)
