# FUNCTIONS

# write a prog that takes list and returns an output of the list
def len_list(lst):
    new = print(len(lst))
    return new

cities = ["kar", "Berlin", "Delhi", "Mumbai", "Washington"]
len_list(cities)

# write a prog, that prints the elements of a lists in a single line
def lin_print(list):
    for item in list:
        print(item, end =" ")

lin_print(cities)
print("")


# write a prog to find a factorial of n (n is a parameter)
def find_fac(n):
    sing = 1
    for i in range(1,n+1):
        sing *=i
    factorial = print(sing)
    return factorial

find_fac(5)


# write a prog to convert UST to pkr
def conv_usd_pkr(usd_val):
    usd = 279
    pkr = 279 * usd_val
    return print(usd_val, "USD = ",pkr, "PKR")

conv_usd_pkr(100)

# HW problem:
def odd_even(number):
    if (number %  2 == 0):
        return print("Even")
    else:
        return print("Odd")

odd_even(589)



# RECURSION - A function calls itself repeatedly (more like a loop) - imp for DSA






