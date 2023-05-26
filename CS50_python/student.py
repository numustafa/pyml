# OOp
def main():
    std = get_student()
    print(f"Hello, {std[0]} from {std[1]}!")

def get_student():
    name = input("What is your name? ")
    house = input("What is your house? ")
    return (name, house)

if __name__ == "__main__":
    main()                  # if I need to run the main function from command line.


# Classes - allows u to invent ur datatypes in python (like lisr, dict, etc), in other words, it allows u to create ur own data type.
# in oop, it is really important feature - it helps u create objects through this, and Python adds the butification of "custom names" to it.




