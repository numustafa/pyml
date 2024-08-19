# STRINGS and CONDITIONAL Statements

# string is a data type, that stores "sequence of characters"

str1 = "This is a string."
str2 = "Apna College"
str3 = "This is a string. \nWe are using escape seq characters to print it in the next line"

'''
ESCAPE SEQUENCE CHARACTERS

tab-space    \t
next line    \n    
'''

print(str3)

'''
STRING OPERATIONS

1- Concatenation         - add 2 saperate strings ("hello" + "World")
2- length of a string    - len(str)
'''
print(str1+str2)         # "This is a string.Apna College"
print(len(str1))         # 17 characters in str1
print(len(str1+" "+str1)) # 17 + 1+ 17 = 35 characters, means space b/w characters is incl in counting


# Indexing - can help in identifying the char but cannot modify it.
print(str1[0])              # always starts from 0...
print(str2[0])

# Slicing - accessing parts of a string **

# Forward slicing - starts from 0
print(str1[2:6])            # is_i (_ means space) 
print(str2[5:len(str2)])    # from 5 till end
# Backward slicing starts from -1
print(str1[-6:-1])


# EX

# write a prog, which takes user input their first name, and print its length
name = input("Enter your first name: ")
print(name, "length of a name is: ",len(name))

# write a prog to find the occurance of $ in a str
print(name.count("$"))

# write a prog, which classify a no as odd or even
num = int(input("Enter the desired no: "))
if (num%2 ==0):
    print("No is Enven")
else:
    print("No is Odd")

# write a prog that classifies the greatest of 3 nos by a user
num1 = int(input("Enter the desired first number: "))
num2 = int(input("Enter the desired Second number: "))
num3 = int(input("Enter the desired Third number: "))

if (num1>=num2 & num1>=num3):
    print("Greatest number is ", num1)
elif (num2 >= num3):
    print("Greatest number is ", num2)
else:
    print("Greatest number is ", num3)


# write a prog if a no is multiple of 7 or not
if (num%7 ==0):
    print(num, " The number is a multiple of 7")
else:
    print(num, " The number is not a multiple of 7")
