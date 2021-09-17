mary_in = open('DATA/mary.txt', "r")
mary_in.close()

try:
    with open('DATA/mary.txt') as mary_in:
        pass
except IOError as err:
    print(err)

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip("\n\r")
        print(line)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print("NORMAL:")
    print(contents)
print('-' * 60)

CHUNK_SIZE = 20
with open('DATA/mary.txt', 'rb') as mary_in:
    i = 0
    while True:
        chunk = mary_in.read(CHUNK_SIZE)
        if len(chunk) == 0:
            break
        print(i, chunk)
        print(mary_in.tell())
        i += 1
print('-' * 60)

with open('DATA/mary.txt', 'r') as mary_in:
    all_lines = mary_in.readlines()
    print("All lines with NL")
    print(all_lines)
print("-" * 60)

with open('DATA/mary.txt', 'r') as mary_in:
    all_lines = mary_in.read().splitlines()
    print("All lines without NL")
    print(all_lines)
print("-" * 60)

with open('DATA/primeministers.txt') as pm_in:
    for raw_line in pm_in:
        line = raw_line.rstrip()
        fields = line.split(':')
        print(fields)
print("-" * 60)

import csv
with open('DATA/primeministers.txt') as pm_in:
    rdr = csv.reader(pm_in, delimiter=":")
    for row in rdr:
        print(row)


import pandas as pd
df = pd.read_table('DATA/primeministers.txt', index_col=0, delimiter=":")
print(df)
df.to_excel("pm.xlsx")
df.to_csv("pm.csv")
df.to_json('pm.json')
