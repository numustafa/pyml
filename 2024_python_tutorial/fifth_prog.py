# Dictionaries and Sets in Python

'''
- Dictionary (mutable) are un-ordered in Key-value pairs. Most operations are similar to lists, with "key" is the main focal poit
- Keys (immutable) can only be Numerics, string, tuple, Boolean or None types & cannot be "duplicated"
- Values (mutable) can be numerics, Lists, dict, strings, tuple, sets...
'''

info = {
    "name": "Naveed",
    "Age" : 32,
    ("a","b") : "a",
    True : "No",
    False : "Yes",
    12 : "yes",
    None : "No",
}
print(info)

# access the dict via key
print(info[12])                  # same - but return error if we get the key wrong
print(info.get(12))              # same - wont return error even if we get the key wrong. to manage workflow
info["name"] = "Ali"
info["surname"] = "No name"
print(info)


# nested dict
info["marks"] = {"A":12, "B":63, "C": 78}
print(info)

# using type-cast method to create a list of info keys
lst = list(info.keys())
print(lst)

# add another key-value pair
info.update({"city":"Berlin"})
print(info)


# SETS

'''
Set {} (mutable) is a collection of unordered elements, No key-value pair like dict 
Each element is unique (no duplication)
Set can store everything, except list and dict - sets elements are immutable (cannot be altered)
'''

collection = {1,"hello", "hello", "hello", 2,3,4}
print(collection)                           # removes duplicates - no order is followed

# To create empty dict
empty_dict = {}
print(type(empty_dict))

# To create empty set
empty_set = set()     
print(type(empty_set))



# EX

# store a following word:meaning into python dict
dictionary = {}       # Empty dict
w1 = {"table": ["a piece of furniture", "list of facts & fig"]}
w2 = {"cat": "a small animal"}

dictionary.update(w1)
dictionary.update(w2)
print(dictionary)

# how many classroom req for each subject: "python", "math", "C++", "math", "ML", "python", "C++","math", "ML"
classroom = set()      # empty set
classroom.add("python")
classroom.add("math")
classroom.add("C++")
classroom.add("python")
classroom.add("ML")
classroom.add("python")
classroom.add("math")
classroom.add("C++")
classroom.add("python")
classroom.add("ML")
print(len(classroom))

# write a prog, that takes marks from user & stor them in  a dict. starts with empty dictionary & add the marks use sub:marks method
marks = {}
chem = int(input("Enter your chemistery marks: "))
marks.update({"Chemistry":chem})
math = int(input("Enter your math marks: "))
marks.update({"Math":math})
eng = int(input("Enter your english marks: "))
marks.update({"English":eng})

print(marks)

# fig out store 9 & 9.0 in a set
new = {9, "9.0"}
new_2 = {("int", 9), ("floats", 9.0)}
print(new)
print(new_2)

