#                                                          1- Function & Var

# Ask usr the name:
name = input("Whats your name? ")

# Remove whitespace from string:
#name= name.strip()

# Capatilize the first letter:
#name = name.capitalize()

name = name.strip().title()
# Print the name:
print("Hello", name)        #comma
print("Hello " + name)      #concatenation
print(f"Hello {name}")      #f-string


#                                                         2- Data Types
# String:
first, mid, last = name.split(" ")
print(first, mid, last)

# Integer:
sum = 1+1
print(sum)

#                                               3- dEVELOPING fUNCTIONS
def hello(to = "World"):        #default value
    print(f"Hello {to}")

def main():
    name = input("Whats your name? ")
    hello(name)
main()




def new_main():
    x = int(input("What is the number? "))
    print(f"The square of {x} is {square(x)}")

def square(n):
    return n*n                # return means that the function gives back a value

new_main()



#                                                         4- Conditional Statements
