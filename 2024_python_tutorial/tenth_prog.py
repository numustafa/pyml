# Object oriented Programing (OOPs) - Object >>> Classes


'''
Class is a blue-print for creating objects. It defines set of attributes & methods that objects will have (when objects get created)
An object is an instance of a class. When you create an object from a class, the object will have the properties (attributes) and behaviors (methods) defined by the class.
There is always a "constructor" (__init__) - if you explicitly dont define it, Python still makes it in the backend and executes it.
Constructor parameter always takes a "self" parameter - self points / ref to the every new object we create => s1, s2,...
Every method in a class takes self as its first parameter.
'''
# creating Class with fixed attributes - all objects will have same name & age
class Student:
    name = "Naveed"
    age = 10

# creating objects (or instances of class) - idea is every student in a class has same name & same age
s1 = Student()  
print(s1.name)  

s2 = Student()
print(s2.name)

s3 = Student()
print(s3.name, s3.age)

# This calss has a constructor, which only prints a message, whenever new object is created.
class Student2:
    name = "Naveed"
    def __init__(self) -> None:
        # print(self) = print(s1)
        print("adding new std to database..")

s1 = Student2()
print(s1)
print(s1.name)     

# This class has a customizable attributes - constructor takes a parameter "fallname" that can take different values
class Student3:
    def __init__(self, fullname):
        self.name = fullname
        print("adding new stds to Database")

'''
Diff b/w Student2 & Student3?
 1- In Student2, every student name is fixed - Naveed   (attribute is fixed)
 2- If we want to add stds with different name, we can add a "fullname" parameter to constructor function
 3- we now, seld corrosponds to objectes, so `self.name` is same as `s1.name`. The diff is, we can create many different s's b/c of self.name
'''

try:
    s2 = Student2("Ali")       # This returns error, b/c the constructor on takes value Naveed.
except:
    s3 = Student3("Ali")
    print(s2.name, s3.name)    # (Naveed, Ali) - whenever we call name from Student2, we get Naveed


# Handelling multiple attributes - name & marks
class Student4:
    def __init__(self, name, marks):
        self.name = name               # name in self.name & altogether the name as the parameter in constructor function - but its a general practice to keep the parameters and self parameters same
        self.marks = marks
        print("adding new stds with marks to Database")

s1 = Student4("Ali", 95)
print(s1.name, s1.marks)
s2 = Student4("Nike", 89)
print(s2.name, s2.marks)
s3 = Student4("Chil", 58)
print(s3.name, s3.marks)
# The data we stored - Ali 95, nike 89 Chil 58 ... is called "Attributes"

'''
Understand the process:
1- Create a class
2- create a constructor
    a- when creating an object, we can pass additional info - like "name" we passed "marks",... - to store unique data for each object
    b- we can access and manipulate the data stored in an object through its attributes
'''

# Example: 
class Student5:
    # Class Attributes
    collage_name = "ABC Collage"
    name = "Anonymous"
    # Default constructors
    def __init__(self):
        pass

    # parameterized constructors (contains object attributes)- once parameters are defined in the objects, Default constructor wont work.
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new stds")

'''
Whenever Class attributes has same parameter as object attribute (name in out Example) - Obj attr > Class attr    precedence
'''

'''
Class is a collection of 2 things - 
    a. Data (attributes) - properties
    b. Methods           - Functions that belongs to objects
'''

class Student6:
    # 1. Class attributes
    collage_name = "ABC Collage"

    # 2. Parameterized Constructor - Object attributes
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    # 3. Class Method - with self parameter
    def welcome(self):
        print("Welcome Student", self.name)
    
    def get_marks(self):
        return self.marks

s1 = Student6("Ali", 65)
s1.welcome()
print(s1.get_marks())





