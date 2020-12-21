from collections import Counter

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

all_similarities = []
for a in all_allergens:
    # find all similarities
    similars = Counter()
    for ing, alle in items:
        if a in alle:
            for x in ing:
                similars[x] += 1

    final = set()
    i = 0
    max_count = 0
    for x, count in similars.most_common(None):
        if i == 0:
            max_count = count

        if count == max_count:
            final.add(x)
        else:
            break

        i += 1
    
    all_similarities.append([a, final])

success = []
for ing in set(all_ingredients):
    failed = False
    for a, i in all_similarities:
        if ing in i:
            failed = True
            break
    
    if not failed:
        success.append(ing)

count = 0
for ing in all_ingredients:
    if ing in success:
        count+=1

print(count)