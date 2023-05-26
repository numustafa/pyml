x = int(input("What is the number? "))
y = int(input("What is the number? "))

# Boolean Expressions:
if x < y:
    print(f"{x} is smaller than {y}") 
elif x > y:
    print(f"{x} is greater than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f" rewrite the integer again!")


if x<y or x>y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")



# Nested if statements:
score = float(input("What is the score? "))

if score>= 90:
    print("The Grade is 'A'")
elif score>= 80:
    print("The Grade is 'B'")
elif score>= 70:
    print("The Grade is 'C'")
elif score>= 60:
    print("The Grade is 'D'")
else:
    print("The Grade is 'F'")


# Parity Check:
n = int(input("What is the number? "))

if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")


def main():
    x = int(input("What is the number? "))
    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

def is_even(n):
    return (n % 2 == 0)

main()