d1 = dict()  # empty dict
d2 = {'a': 5, 'm': 2, 'c': 19}
print(d2.keys())
print(d2.values())
print(d2.items())
d2['d'] = 17
d2['a'] = 0
print(d2)
print(d2['m'], d2['c'])
print(d2.get('x'))
print(d2.get('x', 0))
print()

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
for code in 'RDU', 'OAK', 'ELM', 'LHR', 'LAX', 'EWR':
    print(code, airports.get(code, 'NOT FOUND'))
print()

more_airports = [
    ('LAX', 'Los Angeles'),
    ('ELM', 'Elmyra/Corning'),
    ('RDU', 'Durham (not Raleigh)'),
]

for code, name in more_airports:
    print(code, airports.setdefault(code, name))

print(airports)

even_more_airports = {
    'MIA': 'Miami',
    'JAX': 'Jacksonville',
    'RDU': 'Durham',
}

airports.update(even_more_airports)
print(airports)
print()

# sort by key
for code, name in sorted(airports.items()):
    print(code, name)

# sort by value (timsort)
for code, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(code, name)
print()

def by_value(e):
    return e[1], e[0]

for code, name in sorted(airports.items(), key=by_value):
    print(code, name)

print(airports.items())

