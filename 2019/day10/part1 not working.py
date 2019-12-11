import copy


with open('input.txt') as f:
    inp = f.read()
# inp = '''.#..#
# .....
# #####
# ....#
# ...##'''


def float_range(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i = float(f'{(i + step):.2f}')


def lcm(x, y):
    for i in range(2, max(x, y)):
        if x % i == 0 and y % i == 0:
            return i

    return 1


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = (x - 1, x + 1, y - 1, y + 2)

    def __repr__(self):
        return '<Asteroid x={0.x} y={0.y}>'.format(self)

    def calculate_sight(self, pr=False):
        gradients = set([200])

        for i in asteroids:
            # draw a line between asteroid and self.
            # check if it intersects with anyone's "area"
            # if it does, add 1 to the counter

            ydist = i.y - self.y
            xdist = i.x - self.x

            if xdist == 0 and ydist == 0:
                gradient = (0, 2)
            elif xdist != 0:
                gradient = (ydist / xdist, 1)
            elif xdist == 0:
                # if pr:
                #     print(i.x, i.y, 'xdist', i.x, self.x)
                gradient = (0, 0)
            # if gradient == 0 and pr:
            #     print(i.x, i.y, gradient)

            if gradient not in gradients and pr:
                print('x', i.x, i.y, gradient)
            gradients.add(gradient)

        if pr:
            print(self.x, self.y, len(gradients), gradients)
        return len(gradients)

            #     yspd = ydist / lcm(xdist, ydist)
            #     xspd = xdist / lcm(xdist, ydist)
            # elif ydist == 0:
            #     xspd = xdist
            #     yspd = 0
            # elif xdist == 0:
            #     yspd = ydist
            #     xspd = 0
            # suby = copy.copy(self.y)
            # subx = copy.copy(self.x)
            # # print(self.x, self.y, i.x, i.y, subx, suby, xdist, ydist, xspd, yspd)
            # count += 1
            # while suby != i.y and subx != i.y:
            #     suby += yspd
            #     subx += xspd
            #     # print((round(subx), round(suby)))
            #     if (round(subx), round(suby)) in asteroid_pos and (round(subx), round(suby)) != (self.x, self.y):
            #         # print('x')
            #         count -= 1
            #         break

        # print(self.x, self.y, count)


asteroids = []
asteroid_pos = []
for ny, y in enumerate(inp.splitlines()):
    for nx, x in enumerate(y):
        if x == '#':
            asteroids.append(Asteroid(nx, ny))
            asteroid_pos.append((nx, ny))

sights = {}
for i in asteroids:
    if i.x == 5 and i.y == 8:
        print(i.calculate_sight())
    sights[i] = i.calculate_sight()

print(max(sights, key=lambda x: sights[x]).calculate_sight(pr=True))
print(max(sights, key=lambda x: sights[x]))
print(sights[max(sights, key=lambda x: sights[x])])
