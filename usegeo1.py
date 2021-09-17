import sys
from jpmc.math import geo

print(geo.circle_area(25))

print(geo.square_area(10))

print(geo.PI)

d = geo.Dog()
d.bark()

for path in sys.path:
    print(path)
