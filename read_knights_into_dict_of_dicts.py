knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_info[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment,
        }

print(knight_info['Lancelot']['color'])

for knight, data in knight_info.items():
    # knight, data = NEXT ITEM OF knight_info
    print(data['title'], knight)
print()

items = ['a', 'b', 'c']
for x in items:
    print(x)

print(knight_info.items())

