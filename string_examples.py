s1 = "spam\n"
print(len(s1), s1)
s2 = 'spam\n'
print(len(s1), len(s2))
s3 = """spam\n"""
s4 = '''spam\n'''

s5 = r"spam\n"  # RAW str

print("Guido's the (retired) BDFL of Python")
print('Guido is the (retired) "BDFL" of Python')

print("""Guido's the "BDFL" of Python""")
print('''Guido's the "BDFL" of Python''')

insert_statement = """
insert into spam (a, b, c)
values ("do", "re", "mi")
"""

print(insert_statement)
print(repr(insert_statement))

s = "29\u00B0"
print(s)
print(repr(s))
print(repr(s.encode()))
print(r"29\u00B0")
print()

actor = "Chris Hemsworth"
print(type(actor))
print(len(actor))  # actor.len()  actor.length() actor.size() actor.num_chars()

print(actor.lower())
print(actor.upper())

print(dir(actor), '\n')

a = actor.lower()
print(actor, a)
print(actor.count('h'))
print(actor.count("is"))
print(actor.lower().count('h'))

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
#   $actor =~ /^Chris/
print()

print("is" in actor)   # + - * / in ==
print("was" in actor)

print(actor)
print(actor.replace('Chris', 'Liam'))
print(actor.replace('h', 'X'))
print(actor.replace('h', 'X', 1))

print('-' * 60)
print("\U0001F92F" * 10)

print(actor.find('worth'))  # -1 on not found
print(actor.index('worth'))  # exception on not found

s = "       All my exes live in Texas        "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "xxyyxxxyyyxyxyxAll my exes live in Texasyyyyyyyxxxxxxxxxx"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()

foo = "xyxyxyxyxyblah"
print(foo.replace('xy', ''))



















