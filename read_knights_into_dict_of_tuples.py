import sys
from pprint import pprint

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
    #               key     value
        knight_info[name] = (title, color, quest, comment)

pprint(knight_info, sort_dicts=False)

new_knights = {knight:value for knight, value in sorted(knight_info.items())}

print(knight_info)

# del knight_info  # explicitly delete an object

# x = 5
# print(sys.getsizeof(x))
# name = 'Bob'
# other_name = "aoweifjaowiejfaowiefjaowiejfaowiejfajiwef"
# print(sys.getsizeof(name), sys.getsizeof(other_name))
# s = 'a'
# print(sys.getsizeof(s))
# s = ''
# print(sys.getsizeof(s))

print(knight_info['Lancelot'][1], '\n')


#   key    value
for knight, data in knight_info.items():
    print(data[0], knight)
