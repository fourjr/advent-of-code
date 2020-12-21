from collections import Counter, defaultdict

with open('input.txt') as f:
    input = f.read()

items = []
all_ingredients = []
all_allergens = set()

for line in input.splitlines():
    ingredients = line.split(' (')[0].split(' ')
    if len(line.split(' (')) > 1:
        allergens = line.split(' (')[1][9:-1].split(', ')
    else:
        allergens = []
    
    all_ingredients+=ingredients
    all_allergens.update(allergens)

    items.append([ingredients, allergens])

all_similarities = defaultdict(set)
for a in all_allergens:
    # find all similarities
    similars = Counter()
    for ing, alle in items:
        if a in alle:
            for x in ing:
                similars[x] += 1
    
    final = []
    i = 0
    max_count = 0
    for x, count in similars.most_common(None):
        if i == 0:
            max_count = count

        if count == max_count:
            all_similarities[x].add(a)
        else:
            break

        i += 1

taken_ing = set()
assignment = {}

while len(assignment) != len(all_allergens):
    # account for a possible chance of sorting getting randomised
    assignment = {}
    for k in sorted(all_similarities, key=lambda x: len(all_similarities[x])):
        values = all_similarities[k]
        for v in values:
            if v not in taken_ing:
                assignment[v] = k
                taken_ing.add(v)
                break

dangerous = []
for k in sorted(assignment.keys()):
    dangerous.append(assignment[k])

print(','.join(dangerous))
