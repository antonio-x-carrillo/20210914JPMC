
def get_message():
    return "Hello, JPMC world"

m = get_message()
print("m:", m)
print("calling function:", get_message())

x = get_message  # 'x' and 'get_message' both bound to function object
print(x)  # does NOT execute get_message()
print(x())

a = 10
b = a

x = get_message
y = get_message()

def say_hello():
    print("Hello, world")
    # return None

say_hello()

def add(a, b):
    return a + b

print(add(10, 15))
x = 15
y = 27
print(add(x, y))
print(add('foo', 'bar'))
print(add([1, 2, 3], [4, 5, 6]))
# print(add('foo', 22)) FAIL!
m = 22
print(add('foo', str(m)))

import typing as T
Numeric = T.Union[int, float]

def iadd(a: Numeric, b: Numeric) -> float:
    return float(a + b)

print(iadd(5, 10))
print(iadd('10',  '15'))

#             pos          opt      named
def do_search(search_term, *files, ignore_case=False):
    print("search term:", search_term)
    print("files:", files)
    print()

do_search('rabbit', 'DATA/alice.txt')
do_search('rabbit', 'file1', 'file2', 'file3', ignore_case=True)

def do_search2(search_term, ignore_case, *files):
    pass

do_search2('rabbit', True, 'file1', 'file2')

x = [5]  # list
x = {5}  # set
x = 5,   # tuple
x = (5,) # tuple
x = 5    # int
x = (5)  # int

def spam(pos1, pos2, *, named1, named2):
    print(pos1, pos2, named1, named2)

spam(5, "foo", named1="blah", named2="barf")
spam(1, 2, named2=3, named1=4)

def config(**values):
    print(values)



















