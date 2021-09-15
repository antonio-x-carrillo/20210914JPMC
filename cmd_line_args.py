import sys  # runtime info

print(sys.argv)   # LIST of words on command line
print(sys.argv[0])  # script name

print(sys.argv[2])
value = int(sys.argv[1])
print(value * 1000)
