# File Input/ output 

'''
Used for Open a file, read data from file, write data in the file & close the file
Types of files: Text files (.txt, .docx, .log), Binary files (.mp4, .mov, .png, .jpeg)
'''

f = open("demo.txt", "r")
data = f.read()         # return data in the form of string
print(data)
print(type(data))
f.close()

# using "with" will auto matically closes the file
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

# using Python built-in lib to delete a file
import os
os.remove("demo.txt")


# Ex

# Create a new file "practice.txt" using python. Add strings in it
# if we open a file using "w" (write mode), it created automatically
with open("practice.txt", "w") as f:
    f.write("Hi Everyone \nwe are learning Python")
    f.write("using File I/O.\nI like programing in Python")

# write a prog, that replaces all python with mathematics from practice.txt
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Python", "mathematics")
print(new_data)

with open("practice.txt", "w") as f:
    data = f.write(new_data)


# search if the word learning exist in a file or not.
with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.find("learning")


# check which line the word learning occur first
def check_line(path):
    word = "learning"
    data = True
    with open(path, "r") as f:
        line_no = 1
        while data:
            data = f.readline()          # read data line-wise
            if (word in data):
                return print(line_no)
            line_no +=1
    return -1


# from a file containing nos saperated by comma (,), print the count of even nos
def check_even_count():
    with open("path", "r") as f:
         data = f.read()
         print(data)              # data still in str
         # convert string to list using split
         nums = data.split(",")
         print(nums)
         count = 0
         for val in nums:
             new_val = int(val)
             if (new_val % 2 == 0):
                 count +=1
        return count




