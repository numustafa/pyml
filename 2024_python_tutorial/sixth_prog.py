# Loops in Python

'''
WHILE Loop - while condition is true, execute 
'''
# print "Hello" 5 times
i = 1
while i <=5:
    print("Hello", i)
    i +=1

print("---------------------END------------------------")

# print nos 1 - 10
i = 0
while i <=10:
    print(i)
    i +=1
print("---------------------END------------------------")

# print 5-1
i = 5
while i>=0:
    print(i)
    i -=1
print("---------------------END------------------------")    



# Ex

# print no from 1 - 100
i = 1
while i <= 100:
    print(i)
    i +=1
print("---------------------END------------------------")    

# print nos from 100 - 1
i = 100
while i >0:
    print(i)
    i -=1
print("---------------------END------------------------") 

# print a multiplication table of a no n
n = int(input("Enter the no: "))
i = 1
while i <=10:
    print(n, " x ", i, " = ", n*i)
    i +=1
print("---------------------END------------------------") 

# print the elements of the list [1,4,9,16,25,36,49,64,80,100] using a loop
lst = [1,4,9,16,25,36,49,64,80,100]
i = 0                                      # this is index (iterator) -  we are traversing over a list
while i <= len(lst) - 1 :
    print("square of", i + 1, "is", lst[i])
    i +=1
print("---------------------END------------------------") 

# search for a no "x" in a tuple (1,4,9,16,25,36,49,64,80,100) using loop
tpl = (1,4,9,16,25,36,49, 36,64,80,100, 36, 360)
no = 36
i = 0                                      # this is index (iterator) -  we are traversing over a list
while i <= len(lst) - 1 :
    if (tpl[i] == no):
        print ("found at index ", i)
    else:
        print("finding...")
    i +=1
print("---------------------END------------------------") 


'''
"BREAK" (to terminate the loop) & "Continue" (terminate the current iteration & restart the loop with new iteration) key words
'''
# print nos 1 - 10 - but loop wont go beyond 6
i = 0
while i <=10:
    print(i)
    if (i == 6):
        break
    i +=1
print("---------------------END------------------------")

# we dont want 5
i = 0
while i <=10:
    if (i == 5):        # at 5, we just terminate the further process and restart it angain with new index - skip the process
        i +=1
        continue
    print(i)
    i +=1
print("---------------------END------------------------")

# skip the process for odd no
i = 0
while i <=10:
    if (i % 2 == 1):
        i +=1
        continue
    print(i)
    i +=1
print("---------------------END------------------------")



'''
For Loops - generally use for sequential traversal (traversing list, string, tuples,...)
'''

#  print the elements of the list [1,4,9,16,25,36,49,64,80,100] using a loop
lst = [1,4,9,16,25,36,49,64,80,100]
for i in lst:
    print(i)
else:
    print("END")

# search for a no "x" in a tuple (1,4,9,16,25,36,49,64,80,100) using loop
tpl = (1,4,9,16,25,36,49, 36,64,80,100, 36, 360)
no = 36

idx = 0
for i in tpl:
    if (i == no):
        print("Found at index: ", idx)
    idx +=1
else:
    print("END")


