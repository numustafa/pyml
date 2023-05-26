# syntax error is your responsibility and ensure u correct it

x = int(input("x: "))
print(f"x is {x}")

# to avoid user entering anything except a number, we use try and except

try:
    y = int(input("y: "))
except ValueError:
    print("Please insert an integer!!")
else:
    print(f"y is {y}")


def main():
    z = get_int()
    print(f"z is {z}")

def get_int():
    while True:
        try:
            z = int(input("z: "))
        except ValueError:
            print("Please insert an integer!!")      # we can also use "pass" instead of print - this will just ignore the erroe msg and continue
        else:
            break             # break out of the loop - we can aslo use return z, as return is stronger than break and returns a value
    return z

main()





