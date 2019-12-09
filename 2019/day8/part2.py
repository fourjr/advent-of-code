from PIL import Image, ImageDraw


colors = [
    (0, 0, 0, 255),  # black
    (255, 255, 255, 255),  # white
    (0, 0, 0, 0)  # transparent
]


w, h = (25, 6)
multiplier = 30
img = Image.new('RGBA', (w * multiplier, h * multiplier))
draw = ImageDraw.Draw(img)
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

cursor = [0, 0]

currzero = []
for ww in range(w):
    for hh in range(h):
        for nl, l in enumerate(layers):
            color = colors[l[hh][ww]]
            draw.rectangle(cursor + [cursor[0] + multiplier, cursor[1] + multiplier], color)
            if color[3] != 0:
                break
        cursor[1] += multiplier
    cursor[1] = 0
    cursor[0] += multiplier

img.save('result.png')
