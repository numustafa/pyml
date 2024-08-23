# OOPs

# Ex: create a student class that takes name & marks of 3 subjects as argument in the constructor & then create a Method to print the avg
class Student1:
    # 1. Class attributes
    collage_name = "ABC Collage"

    # 2. Parameterized Constructor - Object attributes
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    # 3. Class Method - with self parameter    
    def get_avg(self):
        avg = (self.marks1 + self.marks2 + self.marks3)/3
        return print("Hi", self.name, " your avg score is: ", avg)

s1 = Student1("Ali", 98,58,86)
s1.get_avg()

# ------------------------------------------------ OR ---------------------------------------------------------------
class Student2:
    # 1. Class attributes
    collage_name = "ABC Collage"

    # 2. Parameterized Constructor - Object Attributes
    def __init__(self, name, marks):                      # marks = [mark1, mark2, mark3]
        self.name = name
        self.marks = marks
    
    # Class Methods
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, " Your avg marks are: ", sum/3)

s1 = Student2("Ali", [98,56,75])
s1.get_avg()

# change the name:
s1.name = "Bali"
s1.get_avg()

# new student
s2 = Student2("RR", [75,65,25])
s2.get_avg()


'''
The Class attributes doesnt do anything infront of object attributes - y not change it into Class methods (without using self)
using a decorator @staticmethod
'''


'''
Ex: Create an Account class with: 
    2 Object attributes - balance & A/c no , 
    Class Methods - Debit (-ve), Credit (+ve) & prinit bal
'''
class BankAccount:
    # 1. Class Attributes
    bank_name = "ABC Bank"

    # 2. Parameterized Constructor - Object Attributes
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    # Class Methods - Debit, Credit & Printing the bal
    def debit(self, amount):
        self.balance -= amount
        print("Eur", amount, "has been debited from your account")
        print("New bal is: ", self.get_bal())
    
    def credit(self, amount):
        self.balance += amount
        print("Eur", amount, "has been credit to your account")
        print("New bal is: ", self.get_bal())
    
    def get_bal(self):
        return self.balance

account1 = BankAccount(1000, 12345)
print(account1.balance, account1.account_no)
account1.debit(500)
account1.credit(800)
account1.credit(1024)
account1.debit(417)
