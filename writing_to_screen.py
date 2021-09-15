a = "hello"
b = 45.390239023

print(a, b)
sep = ' '
end = '\n'
print(str(a) + sep  + str(b) + end)
print()   # print(end)
print(a, b, sep="/")
print(a, b, sep="#")
print(a, b, sep='')

print("starting...", end='')
# time-consuming code here
print("done")

#  "blah blah {:fmt} blah blah {:fmt}".format(p1, p2)
#  f"blah blah {p1:fmt} blah blah {p2:fmt}"
print()
print("str is {} and number is {}".format(a, b))
print(f"str is {a} and number is {b}")
print()
print("number is {:.2f}".format(b))
print(f"number is {b:.2f}")

c = 123
print("Number is >{:6d}<".format(c))
print(f"Number is >{c:6d}<")

print("Number is {:06d}".format(c))
print(f"Number is {c:06d}")
print()

animal = "wombat"
print(f"|{animal:@<10s}|")
print(f"|{animal:_>10s}|")
print(f"|{animal::^10s}|")

print(f"2 plus 2 is {2 + 2}")


