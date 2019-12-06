with open('input.txt') as f:
    inp = f.read().splitlines()


class Planet:  # parent is essentially the same as orbit
    def __init__(self, name, parent):
        self.name = name
        self.parent_name = parent

    @property
    def parents(self):
        if self.parent:
            return [self.parent] + self.parent.parents
        else:
            return []

    @property
    def parent(self):
        if self.parent_name:
            return planets[self.parent_name]

    def __repr__(self):
        fmt = '<Planet name={0.name}'
        if self.parent:
            fmt += ' parent={0.parent}>'
        else:
            fmt += '>'
        return fmt.format(self)

    def __str__(self):
        return self.name


planets = {'COM': Planet('COM', None)}
for i in inp:
    name = i.split(')')[1]
    parent = i.split(')')[0]
    planets[name] = Planet(name, parent)

my_parents = planets['YOU'].parents
santa_parents = planets['SAN'].parents
target = [i for i in my_parents if i in santa_parents][0]
print(my_parents.index(target) + santa_parents.index(target))
