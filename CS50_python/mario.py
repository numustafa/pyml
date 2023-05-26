# printing a blo9ck of hashes in the shape of a 3*3 cube
def main():
    print_square(3)

def print_square(size):

    # For each row in a 3*3 cube
    for i in range (size):
        # For each column in a 3*3 cube
        for j in range (size):
            print("#", end="")
        print()                # Print a new line after each row of hashes

main()
print("------------------\n")

# Another approach
def main():
    print_squaree(3)

def print_squaree(size):         # this function print rows of hashes
    for i in range(size):
        print_line_width(size)

def print_line_width(width):     # this function print a line of hashes of a given width
    print("#" * width)

main()
