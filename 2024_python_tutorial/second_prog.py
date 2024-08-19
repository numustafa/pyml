# Variable & data Types Continues ... 
# operators
'''
Arithmetic operators                 (+,-,*,/,//,%,**)
Relational / Comparision Operators   (==, !=, >, <, >=, <=)
Assignment Operators                 (=, +=, -=, *=, /=, %=, //=, **=)
Logical Operators                    (not, and, or)                - operator precedence (not > and > or)
Membership Operators                 (in, notin)
Identity Operators                   (is, isnot)
Bitwise Operator                     (&, |, ^)    - AND, OR, XOR
'''

# Arithmetic operators
a = 20                  # Assignment operator
b = 50
c = 2
print (b%a)        # to find the remainder
print(a**c)

# Relational / Comparision Operators  -  Ans is always gives output as boolean
print (a == b) # F
print (a != b) # T
print( b>=a)   # T

a -= 10
print(a)


# Logical Operators
# not operator always return the opposite
print(not True)  # F
print(not (a>b)) # T - in reality, its false

val1 = True
val2 = False
val3 = True
print("AND operator (both are not same): ", val1 and val2) 
print("AND operator (both are same): ", val1 and val3)
print("OR operator (either one is true):", val1 or val2)
print("OR operator (T or F):", (a<b) or (a == b))

# Ex

# write a prog, takes inputs 2 nos, and prints the sum of those 2 nos
num1 = int(input("Enter first no: "))
num2 = int(input("Enter second no: "))
print("The sum of first number & second number is: ", num1+num2 )

# write a prog, that take inputs as a side of a square, and print its area
side = int(input("Enter the side of a square: "))
print("Area of a square is: ", side**2)

# write a prog, that takes 2 floats and gives an avg of those 2
num1 = float(input("Enter first no: "))
num2 = float(input("Enter second no: "))
print("The avg of first number & second number is: ", (num1+num2)/2 )