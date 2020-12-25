with open('input.txt') as f:
    data = list(map(int, f.readlines()))

card_public_key = data[0]
door_public_key = data[1]

def get_loop_size(sub_number, result):
    value = 1
    n = 0
    while True:
        value *= sub_number
        value %= 20201227

        n += 1
        if value == result:
            return n

def transform(sub_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= sub_number
        value %= 20201227

    return value

loop_s = get_loop_size(7, card_public_key)
print(transform(door_public_key, loop_s))