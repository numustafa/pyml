import sys

#print("Hello, my name is", sys.argv[1])      # argv[0] is the name of the file itself, argv[1] is the first command line argument

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Missing command line argument!!")
    sys.exit(1)     # exit the program with a status of 1 (error)

