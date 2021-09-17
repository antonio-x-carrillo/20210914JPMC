x = 100  # GLOBAL variable

def main():
    spam()
    print("in main(): x is", x)

def spam():
    x = 1000  # LOCAL variable
    y = 50  # LOCAL var
    if y > 10:
        name = 'Fred'
    print("name is", name)
    print("in spam", x, y)

main()

# local nonlocal global builtin

def outer():
    x = 5

    def inner():
        print(x)  # x is local to outer, but nonlocal to inner

