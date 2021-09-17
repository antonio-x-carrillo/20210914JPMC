from collections import Counter

with open('DATA/breakfast.txt') as food_in:
    foods = food_in.read().splitlines()
    counts = Counter(foods)
    counts['donuts'] += 1

print(counts)
print(counts.most_common(3))
