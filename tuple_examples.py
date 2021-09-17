
"""
struct person {
    char *fname;
    char *lname;
    int age;
}
"""

person = ("Bill", 'Gates', 'Microsoft', '1955-10-28')
person = "Bill", 'Gates', 'Microsoft', '1955-10-28'

print(person)

print(person[0], person[1])
# person[0] = "William"   FAIL

first_name, last_name, product, dob = person
#  first_name = person[0], last_name = person[1], etc.

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'git', 'Linux', '1969-12-28'),
]
print(people[0])
print(people[0][0])
print(people[0][0][0])

for person in people:
    print(type(person), person, person[-1])
print("-" * 60)

#   tuple-of-variables = iterable
for first_name, last_name, *product, dob in people:
    # field1 field2 ... = <next-element>
    print(first_name, last_name, product, dob)
print()

for first_name, last_name, *_ in people:
    # field1 field2 ... = <next-element>
    print(first_name, last_name)
print()

values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)

u, *v, w, x, y = values
print(u, v, w, x, y)






