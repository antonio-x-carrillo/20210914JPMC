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

print(cities[0], cities[2], cities[-1], cities[-3])

print(cities[0:3])
print(cities[3:7])
# L[start:stop]
# L[:stop]  # start is 0
# L[start:] # end is len(L)
# L[start:stop:step]
print(cities[:3])
print(cities[8:])
print(cities[-4:])

# slice works on list, tuple, str, bytes

actor = "Chris Hemsworth"
print(actor[:5])
print(actor[6:9])
print(actor[-5:])

s = "abcdefghijklmnopqrstuvwxyz"
print(s)
print(s[5:12])
print(s[5:12:2])
print(s[::2])
print(s[1::2])

for city in cities:
    print(city.upper())

# for VAR ... in ITERABLE:
#     ...
#     ...

print(len(cities), min(cities), max(cities))
print(sorted(cities))
print(min("applesauce"), max("applesauce"))

data = [5, 8, 4.3, 27.6, -100]
print(sum(data))
print(min("apricotApple"))

print(cities, '\n')
rc = reversed(cities)
print(rc)
for city in rc:
    print(city.upper())
print()

# for VAR in ITERABLE:
for i, city in enumerate(cities):
    if i % 2 == 0:
        print(i, city)
print()
ec = enumerate(cities)
print(ec, list(ec))


