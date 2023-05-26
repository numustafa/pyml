class Student:
    def __init__(self, name, house, patronus):                 # This dunderscore init dunderscore is a special function, called a constructor/ instance method. It is a function that gets called when u create a new object of the class.
        if not name:
            raise ValueError("You must provide a name.")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("You must provide a valid house.")
        self.name = name                  # if u want to initialize the contents of an object from a class, u can do it here.
        self.house = house               # Rember!! later we use a function Student(name, house) - this is a def version OF sTUDENT FUNCTION, where we store the values!!
        self.patronus = patronus
# instead of using a get_student outside the claas, we can use a function inside the class, called a method. (its an organization thing, not a technical thing)
    @classmethod                    # this is a decorator, which is a special function that modifies the behavior of another function. It is a function that gets called when u create a new object of the class.
    def get_std(cls):
        name = input("What is your name? ")
        house = input("What is your house? ")
        patronus = input("What is your patronus? ")
        return cls(name, house, patronus)        
    
    def __str__(self):                   # this is a special function, called a string method. It is a function that gets called when u try to print an object of the class.
        return f"{self.name} is in {self.house} with {self.patronus}."

# All my student related to code is in the class, together
def main():
    std = Student.get_std()
    #print(f"Hello, {std.name} from {std.house}!")
    print(std)

if __name__ == "__main__":
    main()

