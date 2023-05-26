# Classes - allows u to invent ur datatypes in python (like lisr, dict, etc), in other words, it allows u to create ur own data type.
# in oop, it is really important feature - it helps u create objects through this, and Python adds the butification of "custom names" to it.

class Student:
    ...
def main():
    std = get_student()
    print(f"Hello, {std.name} from {std.house}!")

def get_student():                         # same function, not using a tuple, but a class!!
    std = Student()                        # std is an object of the class Student
    std.name = input("What is your name? ") # if it was a dict or list or tuple, we can use std["name"] or std[0] , but here we have attributes, and syntax for class attriburtes is ".", simply a dot
    std.house = input("What is your house? ")
    return std                             # return the object std

if __name__ == "__main__":
    main()


