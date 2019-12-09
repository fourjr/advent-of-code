w, h = (25, 6)
with open('input.txt') as f:
    inp = f.read()


def create_combined_layer(l):
    combined_layer = []
    for x in l:
        combined_layer += x
    return combined_layer


cursor = (0, 0)
layers = []
for n in inp:
    if not layers or (len(layers[-1]) == h and len(layers[-1][-1]) == w):
        layers.append([[]])
    if not layers or len(layers[-1][-1]) == w:
        layers[-1].append([])
    layers[-1][-1].append(int(n))

currzero = []
for n, l in enumerate(layers):
    combined_layer = create_combined_layer(l)
    currzero.append(len(list(filter(lambda x: not x, combined_layer))))

combined_layer = create_combined_layer(layers[currzero.index(min(currzero))])
print(len(list(filter(lambda x: x == 1, combined_layer))) * len(list(filter(lambda x: x == 2, combined_layer))))
