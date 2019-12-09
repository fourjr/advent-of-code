import random
from PIL import Image, ImageDraw


colors = [
    (0, 0, 0, 255),  # black
    (255, 255, 255, 255),  # white
    (0, 0, 0, 0)  # transparent
]


w, h = (25, 6)
multiplier = 30
img = Image.new('RGB', (w * multiplier, h * multiplier))
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

count = 0
possible_ww = range(0, w * multiplier, multiplier)
possible_hh = range(0, h * multiplier, multiplier)
possibles = [(ww, hh) for ww in possible_ww for hh in possible_hh]
while len(possibles):
    loc = random.choice(possibles)
    possibles.remove(loc)
    for l in layers:
        color = colors[l[loc[1] // multiplier][loc[0] // multiplier]]
        draw.rectangle((loc, (loc[0] + multiplier - 1, loc[1] + multiplier - 1)), color)
        if color[3] != 0:
            if color[0] != 0:
                img.save(f'frames/{count}.png')
                count += 1
            break

for _ in range(15):
    # add more frames for the gif
    img.save(f'frames/{count}.png')
    count += 1
# ffmpeg -i frames/%01d.png output.gif -framerate 20

img.save('result.png')
