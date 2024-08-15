print("Hello World!")
print("My name is Naveed")
print("Hello World!","My name is Naveed", 25,30, 25-30)

# Variables
name = "Naveed"             # string
age = 32                    # Integer
price = 25.99               # Floats
print(name, age, price)
print("My name is: ", name)
print("My age is: ", age)

age2 = age                  # possible b/c of assignment rule 
print(age, "type of age: ", type(age), age2)                  

# Data Types (Integers, Strings, Floats, Boolean, None)
age = 23       # int
old = False    # Boolean
a = None       # None
print(type(age), type(old), type(a))  

# EX: Print Sum
a = 5
b = 25
sum = a+b
diff = a-b
print("Sum of a & b: ", sum)
print("Diff of a & b: ", diff)

# Ex: Expression Execution
a,b,c = "2",3,4.1
txt = "@"
print("String & numeric together with *: ", txt*b)
print("string & string can operate with + (concatination): ", (a+txt)*b)
print("multiplication or division with float results in always floats: ", b*c)