# Question 1: Arithmetic Operations Program

def arithmetic(a, b):

    # Addition
    print("Addition:", a + b)

    # Subtraction
    print("Subtraction:", a - b)

    # Multiplication
    print("Multiplication:", a * b)

    # Division
    print("Division:", a / b)

    # Modulus/Floor Division
    print("Modulus:", a // b)

# Function call
arithmetic(5, 7)



# Question 2: Increment and Decrement Program

# Taking input from user
num = int(input("Enter a number: "))

# Increment operation
num = num + 1
print("After increment:", num)

# Decrement operation
num = num - 1
print("After decrement:", num)



# Question 3: Equal and Not Equal Operators

# Taking two numbers as input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Checking equality
if num1 == num2:
    print("Both numbers are equal")

else:
    print("Both numbers are not equal")



# Question 4: Relational Operators Program

# Taking input values
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Relational operator checks
print("a < b:", a < b)
print("a <= b:", a <= b)
print("a > b:", a > b)
print("a >= b:", a >= b)



# Question 5: Find Larger and Smaller Number

a = 15
b = 8

# Checking larger and smaller number
if a > b:
    print("Larger number is:", a)
    print("Smaller number is:", b)

else:
    print("Larger number is:", b)
    print("Smaller number is:", a)
