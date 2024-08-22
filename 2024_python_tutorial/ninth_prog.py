# File Input/ output 

'''
Used for Open a file, read data from file, write data in the file & close the file
Types of files: Text files (.txt, .docx, .log), Binary files (.mp4, .mov, .png, .jpeg)
'''

f = open(demo.txt, "r")
data = f.read()         # return data in the form of string
print(data)
print(type(data))
