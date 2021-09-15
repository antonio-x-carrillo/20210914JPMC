
#  int float complex bool

i1 = 100
i2 = 0b100   # 0b10010011
i3 = 0x100   # 0xDeadBeef   0xABCD 0x12AB
i4 = 0o100

print(i1, i2, i3, i4)
print()

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.2903e44

a = 19
b = 6
print(a + b)
print(a - b)
print(a * b)
print(a / b)   # true division
print(a // b)  # floored division
print(a % b)   # modulus  (remainder)
print(a ** b)  # exponentiation
print(a ** .5)
print()

x = 5
x += 1  # x = x + 1
x *= 2
x /= 3  # x = x / 3
print(x)

print(type(1), type(1.0))
print("foo".upper())

x = 123
y = "456"
print(str(x) + y)
print(x + int(y))
print(int("3903"))  #  int x = new int("3903");
print(float(x))

# int() float() bool() complex()
# str() bytes()
# list() tuple() dict() set()














