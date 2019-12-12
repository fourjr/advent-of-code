import copy
from dataclasses import dataclass, field


with open('input.txt') as f:
    inp = f.read().splitlines()

@dataclass
class Coordinates:
    x: int = 0
    y: int = 0
    z: int = 0

    def __hash__(self):
        return hash(f'{self.x},{self.y},{self.z}')

@dataclass
class Moon:
    position: Coordinates
    velocity: Coordinates = field(default_factory=Coordinates)
    previous_positions = list()

    def apply_gravity(self):
        for m in moons:
            if self.position.x > m.position.x:
                self.velocity.x -= 1
            elif self.position.x < m.position.x:
                self.velocity.x += 1

            if self.position.y > m.position.y:
                self.velocity.y -= 1
            elif self.position.y < m.position.y:
                self.velocity.y += 1

            if self.position.z > m.position.z:
                self.velocity.z -= 1
            elif self.position.z < m.position.z:
                self.velocity.z += 1

    def apply_velocity(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z

    @property
    def potential_energy(self):
        return abs(self.position.x) + abs(self.position.y) + abs(self.position.z)

    @property
    def kinetic_energy(self):
        return abs(self.velocity.x) + abs(self.velocity.y) + abs(self.velocity.z)

    @property
    def total_energy(self):
        return self.potential_energy * self.kinetic_energy

    def __repr__(self):
        return 'Moon(position={0.position}, velocity={0.velocity}, potential={0.potential_energy}, kinetic={0.kinetic_energy}, total={0.total_energy})'.format(self)


moons = []
for i in inp:
    values = i.split(', ')
    new_values = []
    for v in values:
        for n, i in enumerate(v):
            if i == '=':
                new_val = v[n + 1:]
                if new_val.endswith('>'):
                    new_val = new_val[:-1]
                new_values.append(int(new_val))
    moons.append(Moon(Coordinates(*new_values)))

rounds = 0
while True:
    counter = 0
    the_position = 0
    for m in moons:
        m.apply_gravity()
    for n, m in enumerate(moons):
        m.apply_velocity()

        if the_position:
            if m.previous_positions[the_position] == m.position:
                counter += 1
        elif n == 0 and m.position in m.previous_positions:
            # print(m.previous_positions)
            print(m.position)
            counter += 1
            the_position = m.previous_positions.index(m.position)
        m.previous_positions.append(m.position)

    rounds += 1
    print('a', counter, rounds)

    if counter == len(moons):
        for m in moons:
            print(m)
        break


print(rounds)
