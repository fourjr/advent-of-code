inp = '171309-643603'

minimum = int(inp.split('-')[0])
maximum = int(inp.split('-')[1])

count = 0

for i in range(minimum, maximum):
    if len(str(i)) == 6:
        maxno = 0
        breakout = False
        repeat = False
        for x in str(i):
            if maxno > int(x):
                breakout = True
                break
            maxno = int(x)
            if not repeat and str(i).count(x) > 1:
                repeat = True

        if not repeat or breakout:
            continue

        count += 1

print(count)
