# in the function above, std.name and std.house are called attributes of the class Student. We can build other attribubes in the classes. 
# Now we call those attributes "instance Variables" - they are variables that are specific to the instance of the class. now we defive 2 var name & house, inside object whose data type is Students.

# with each class, we get a function of a same name!
class Student2:
    def __init__(self, name, house, patronus):                 # This dunderscore init dunderscore is a special function, called a constructor/ instance method. It is a function that gets called when u create a new object of the class.
        if not name:
            raise ValueError("You must provide a name.")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("You must provide a valid house.")
        self.name = name                  # if u want to initialize the contents of an object from a class, u can do it here.
        self.house = house               # Rember!! later we use a function Student(name, house) - this is a def version OF sTUDENT FUNCTION, where we store the values!!
        self.patronus = patronus
    

    def __str__(self):                   # this is a special function, called a string method. It is a function that gets called when u try to print an object of the class.
        return f"{self.name} is in {self.house} with {self.patronus}."


def main():
    std = get_student()
    #print(f"Hello, {std.name} from {std.house}!")
    print(std)

def get_student():                         
    name = input("What is your name? ")
    house = input("What is your house? ")
    patronus = input("What is your patronus? ")
    student = Student2(name, house, patronus)        # here we are creating an object of the class Student2, and passing the 2 variables name & house to the class constructor
    return student                            

if __name__ == "__main__":
    main()