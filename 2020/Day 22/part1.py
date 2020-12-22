
with open('input.txt') as f:
    data = f.read()

p1, p2 = [i for i in data.split('\n\n')]
p1 = [int(x) for x in p1.splitlines()[1:]]
p2 = [int(x) for x in p2.splitlines()[1:]]

while len(p1) > 0 and len(p2) > 0:
    play1 = p1.pop(0)
    play2 = p2.pop(0)
    if play1 < play2:
        p2.append(play2)
        p2.append(play1)
    elif play1 > play2:
        p1.append(play1)
        p1.append(play2)
    else:
        print('error', play1, play2)

score = 0
if len(p1) > 0:
    winner = p1
elif len(p2) > 0:
    winner = p2
for n, i in enumerate(winner):
    score += i * (len(winner) - n)

print(score)