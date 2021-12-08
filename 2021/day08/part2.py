from aoc import get_input_as, submit
from collections import defaultdict

inp = get_input_as()

SEGMENTS = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

F_SEGMENTS = {
    hash(''.join(sorted('abcefg' ))): 0,
    hash(''.join(sorted('cf'     ))): 1,
    hash(''.join(sorted('acdeg'  ))): 2,
    hash(''.join(sorted('acdfg'  ))): 3,
    hash(''.join(sorted('bcdf'   ))): 4,
    hash(''.join(sorted('abdfg'  ))): 5,
    hash(''.join(sorted('abdefg' ))): 6,
    hash(''.join(sorted('acf'    ))): 7,
    hash(''.join(sorted('abcdefg'))): 8,
    hash(''.join(sorted('abcdfg' ))): 9,
}
ans = 0
count = 0
for i in inp:
    patterns, output = i.split(' | ')
    mapping = {
        'a': None,
        'b': None,
        'c': None,
        'd': None,
        'e': None,
        'f': None,
        'g': None,
    }
    full_mapping = defaultdict(list)
    for x in patterns.split(' '):
        full_mapping[len(x)].append(x)
    calc_1_7 = [x for x in full_mapping[3][0] if x not in full_mapping[2][0]]
    assert len(calc_1_7) == 1
    mapping['a'] = calc_1_7[0]

    a_or_f = list(full_mapping[2][0])
    calc_1_4 = [x for x in full_mapping[4][0] if x not in full_mapping[2][0]]
    assert len(calc_1_4) == 2
    b_or_d = calc_1_4

    in_9 = calc_1_7 + a_or_f + b_or_d

    # now: a is confirmed, b/c/d/f is unsure

    # find 9 -> g
    for v in full_mapping[6]:
        if all(x in v for x in in_9):
            # this is 9
            g_val = [x for x in v if x not in in_9]
            assert len(g_val) == 1
            mapping['g'] = g_val[0]
            break

    in_8 = in_9 + g_val
    # find 8 -> e
    e_val = [x for x in full_mapping[7][0] if x not in in_8]
    assert len(e_val) == 1
    mapping['e'] = e_val[0]

    # find 5/6
    # finding 0 and 6
    cleared = []
    for j in full_mapping[6]:
        clean = ''.join(x for x in j if x not in (mapping['a'], mapping['e'], mapping['g']))
        cleared.append(set(clean))

    # fnding 5
    two = None
    three = None
    five = None
    for j in full_mapping[5]:
        clean = ''.join(x for x in j if x not in (mapping['a'], mapping['e'], mapping['g']))
        if len(clean) == 3:
            if set(clean) in cleared:
                five = j
            else:
                three = j
        else:
            two = j

    assert five is not None

    # get 2/3
    two_three = {}
    for j in full_mapping[5]:
        if j != five:
            clean = ''.join(x for x in j if x not in (mapping['a'], mapping['e'], mapping['g']))
            two_three[len(clean)] = clean

    assert len(two_three.keys()) == 2

    # two_three[2] = from 2
    # two_three[3] = from 3
    # dif is F
    # -> find f
    f_val = [x for x in two_three[3] if x not in two_three[2]]
    assert len(f_val) == 1
    assert f_val[0] in a_or_f
    mapping['f'] = f_val[0]

    clean_func = lambda j: ''.join(x for x in j if x not in (mapping['a'], mapping['e'], mapping['g'], mapping['f']))
    clean5 = clean_func(five)
    clean3 = clean_func(three)
    clean9 = clean_func(in_9)
    assert len(clean9) == 3

    c_val = [x for x in clean9 if x not in clean5]
    assert len(c_val) == 1
    mapping['c'] = c_val[0]

    b_val = [x for x in clean9 if x not in clean3]
    assert len(b_val) == 1
    mapping['b'] = b_val[0]

    used_letters = []
    for k, v in mapping.items():
        if isinstance(v, str):
            used_letters.append(v)
    d_val = [x for x in 'abcdefg' if x not in used_letters]
    assert len(d_val) == 1
    mapping['d'] = d_val[0]

    flip_mapping = {}
    for k, v in mapping.items():
        flip_mapping[v] = k
    curr_ans = ''
    for x in output.split(' '):
        hashed_val = hash(''.join(sorted(flip_mapping[u] for u in x)))
        curr_ans += str(F_SEGMENTS[hashed_val])
    ans += int(curr_ans)

submit(ans)
