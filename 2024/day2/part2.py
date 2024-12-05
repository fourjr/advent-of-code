import aoc


reports = aoc.get_input_as(callback=lambda i: list(map(int, i.split(' '))), sep='\n')


def test_report(report):
    sign = None
    prev = None
    for level in report:
        if prev is not None:
            difference = level - prev
            if abs(difference) > 3 or abs(difference) < 1:
                return False
            current_sign = difference // abs(difference)
            if sign is not None:
                if sign != current_sign:
                    return False
            else:
                sign = current_sign
        prev = level

    return True


count = 0
for report in reports:
    valid = test_report(report)
    if valid:
        count += 1
    else:
        # try removing one by one
        for n in range(len(report)):
            valid = test_report(report[:n] + report[n+1:])
            if valid:
                count += 1
                break

print(count)
