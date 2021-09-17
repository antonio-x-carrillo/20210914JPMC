mary_countries = ['India', 'UK', 'US', 'Malta', 'New Zealand', 'Vietnam', 'Peru']

anuj_countries = ['UK', 'Malta', 'India', 'Vietnam', 'Spain', 'France',
                  'India', 'Mali', 'Burkina Faso', 'India']

# explicit
mary = set(mary_countries)
anuj = set(anuj_countries)
mary.add('Paraguay')
mary.add('Paraguay')
mary.add('Uruguay')

print("Mary:", mary)
print("Anuj:", anuj)
print()

for country in 'India', 'Paraguay', 'Mali':
    print(country, country in mary, country in anuj)
print()

print("Common:", mary & anuj)  # intersection
print("Not common:", mary ^ anuj)  # Xor
print("Both (all):", mary | anuj)  # union
print("only Mary:", mary - anuj)
print("only Anuj:", anuj - mary)


# # literal = 'implicit'
# hues = ['red', 'green', 'blue']  # literal list
# shades = 'red', 'green', 'yellow'  # literal tuple
# colors = {'red', 'blue', 'purple', 'red', 'red', 'blue'}  # literal set
# color_info = {'red': 5, 'blue': 10, 'purple': 7}  # literal dictionary
# print(colors)