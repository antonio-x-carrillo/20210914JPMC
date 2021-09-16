list1 = list()  # empty list
print(list1, type(list1))

list2 = ['wombat', 'koala', 'wallaby']
print(list2, len(list2), list2[0], list2[2])

list3 = []  # empty list

cities = ['Durham', 'San Francisco', 'Jersey City',
        'Columbus', 'Wilmington', 'Houston']

print(cities)

cities.append('Bowie')
print(cities)
cities.append('Columbia')
cities.append('Glen Burnie')
print(cities)
cities.insert(0, 'Greenbelt')
cities.insert(4, 'Ellicott City')
print(cities)

more_cities = ['Wheaton', 'College Park', 'Takoma']
cities.extend(more_cities)
print(cities)

#  L.append(obj) L.insert(pos, obj)  L.extend(iterable)
city = 'Glen Burnix'
try:
    index = cities.index(city)
except ValueError as err:
    print(city, "not found")
else:
    del cities[index]
print(cities)
print(len(cities))

try:
    cities.remove('Columbus')
except ValueError as err:
    print(err)
print(cities, '\n')

c = cities.pop()
print(c)
print(cities)

c = cities.pop(3)
print(c, cities)

#  del L[pos]  L.remove(value)  value = L.pop(pos)
print(cities[0])
print(cities[4])
print(cities[len(cities) - 1])
print(cities[-1])
print()

for city in cities:
    # city = next(cities)
    print(city.upper())
print()

for note in 'do', 're', 'mi':
    print(note)
print()

name = "John"
for letter in name:
    print(letter)
print()

print(cities)


