# LISTS & TUPLES in Python

'''
- In comparision with String (which stores characters), List stores any type of data.
- Strings are immutable but list are mutable (elements of a list can be altered).
- Slicing (like string) is also possible in lists, and rules of indexing remains same.
'''

lst_num = [2,3,89,-1,78,-100,52.6]
lst_str = ["naveed","a","b", "f", "e"]
lst_lst = [["naveed"], ["a","b", "f", "e"]]
print(lst_num.append(4))
print(lst_num.sort())
print(lst_num)
print(lst_num.sort(reverse=True))      # sort in desc order
print(lst_num)

print(lst_str.sort())
print(lst_str)
lst_str.reverse()
print(lst_str)

# alteration
lst_num.insert(3, 890)     # insert at index 3 a value of 890
print(lst_num)


# TUPLES

'''
Like strings (unlike lists) Tuples are immutable
similar operation like lists - count, indexation, sort, slicing,...
'''

tup1 = (1,)      # tuple
new = (1)        # not a tuple - just an integer


# Ex

# write a prog, ask usr to enter names of 3 fav movies, and store them in a list

movie_lst = []                                               # Empty list
movie1 = input("Enter the name of your most fav movie: ")
movie_lst.append(movie1)
movie2 = input("Enter the name of your 2nd most fav movie: ")
movie_lst.append(movie2)
movie3 = input("Enter the name of your 3rd most fav movie: ")
movie_lst.append(movie3)

print(movie_lst)

# write a prog, to check if a list contains palindrome of elements - use copy() method
# palindrome means, original & reverse are same. e.g => ["m", "a", "a", "m"], [1,2,1]
lst1 = [1,2,3]
lst2 = [1,2,1]

copy_lst2 = lst2.copy()        # step-1: copy list
copy_lst2.reverse()            # step-2: reverse the copied list
if (lst2 == copy_lst2):        # step-3: check if its == original list
    print("Palindrome")
else:
    print("not palindrome")


# write a prog, that cout the no of A-grades in the following grade_tuple + store the values in a list and sort them
grade_tuple = ("C","D","A","A","B","B","A")
print(grade_tuple.count("A"))                 # 3

grade_lst = []
for grade in grade_tuple:
    grade_lst.append(grade)
grade_lst.sort()
print(grade_lst)





