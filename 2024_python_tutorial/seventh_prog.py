# Range
print(range(5))

seq = range(5)                                   # starts = 0, ends = 5 (not incl) - step size = 1 (default)
print(seq[0],seq[1], seq[2], seq[3], seq[4])

for i in range(10):
    print(i)
else:
    print("END")

for i in range(2, 11, 2):
    print(i)
else:
    print("END")

# print the multiplication of a table n
num = int(input("Enter the number: "))
for i in range(1,11):
    print(i," x ", num, " = ", i*num)
else:
    print("END")



# EX
# write a prog, to find the sum of first n natural no - use while
sum = 0
i = 1
while i <= num:
    sum +=i
    i += 1
print(sum) 

# write a prog, to find a factorial of first n natural nos - for loop
fac = 1
for i in range(1,num+1):
    fac *= i
    print("Factorial of ", i, "is ",fac)
else:
    print("END")
