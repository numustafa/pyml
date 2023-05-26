std = ["Hermione", "Harry", "Ron", "Ginny"]
print(std[0]) 
print(std[1])
print(std[2])
print(std[3])
print(std[-1])

# creating a iteration to print the content of the list, using for loop

for s in std:
    print(s)


# want to iterate the list using nos, we use len() function - to use range() function
for i in range(len(std)):
    print(i+1, std[i])

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
students = {"Hermonie": "Gryffindor", 
            "Harry": "Gryffindor", 
            "Ron": "Gryffindor", 
            "Ginny": "Slytherin"}
print(students["Hermonie"])         # to print the value of the key

for student in students:
    print(student)                   # to print the key

for student in students:
    print(f"{student} is in {students[student]}")  # to print the key and value


students = [
    {"name": "Hermonie", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
    {"name": "Luna", "house": "Ravenclaw", "patronus": "Hare"},
]

for student in students:
    print(f"{student['name']} is in {student['house']} and their patronus is {student['patronus']}")
    






