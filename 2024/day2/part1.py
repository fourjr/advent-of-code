import aoc


reports = aoc.get_input_as(callback=lambda i: list(map(int, i.split(' '))), sep='\n')

count = 0
for report in reports:
    sign = None
    prev = None
    success = True
    for level in report:
        if prev is not None:
            difference = level - prev
            if abs(difference) > 3 or abs(difference) < 1:
                success = False
                break
            current_sign = difference // abs(difference)
            if sign is not None and sign != current_sign:
                success = False
                break
            else:
                sign = current_sign
        prev = level
    print(report, success)
    if success:
        count += 1

print(count)
