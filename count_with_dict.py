
counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()
        if food not in counts:
            counts[food] = 0
        counts[food] = counts[food] + 1
        #  counts[food] += 1
        # counts[food] = counts.get(food, 0) + 1

print(counts)