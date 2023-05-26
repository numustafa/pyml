#                                                              Loops

print(" meow,"*4)

# while loop - allows qs everythime it loops or checks it the condition is true or false everytime it loops
i = 3
while i != 0:
    print("meow ---", i)
    i -= 1                      # i = i - 1 (decrementing)

while i <=3:
    print("meow ---", i)
    i += 1                      # i = i + 1 (incrementing)

print("--------------------"*3)
# for loop - allows to loop over a collection of items (list, string, tuple, dictionary, set)
for i in [0,1,2,3]:
    print("meow ---", i)


for _ in range(3):                 # range(3) = [0,1,2]
    print("meow       ", _)


# using dictionary
student = {"Alice": 25, 'Bob': 27, "Carol": 29}             # key: value     Student, their marks in a test
print(student.items())                                      # dict_items([('Alice', 25), ('Bob', 27), ('Carol', 29)])
print(student["Alice"])                                     # prints Alice's marks

for i in student:
    print(i)                                                # prints only the keys


print("mewo\n" *3, end = "")                                # end = "" - to print in the same line 

# writing function for 2 steps to avoid confusion
def main():
    number = get_number()
    meow(number)                                      # calling the function - though function mewo doesnt defined yet

def get_number():
    n = int(input("Number: "))
    while True:
        if n >= 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
