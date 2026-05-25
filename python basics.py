# Question 1: Program to print name using user input

name = input("Enter a name: ")
print("My name is", name)



# Question 2: Single-line and Multi-line Comments

# This is a single-line comment

"""
This is a
multi-line comment
"""

print("hello everyone")



# Question 3: Define variables for different data types

# String variable
Name = "Mounika"

# Integer variable
Salary = 28000

# Boolean variable
Btech = True

# Character/String variable
Grade = 'A'

# Float variable
Cgpa = 8.59

# Double/Float variable
Annual_salary = 27000.5678

# Printing all variables
print("Name:", Name)
print("Salary:", Salary)
print("Btech:", Btech)
print("Grade:", Grade)
print("Cgpa:", Cgpa)
print("Annual_salary:", Annual_salary)



# Question 4: Local and Global Variables

# Global variable
name = "mounika"

def show():

    # Local variable
    name = "Banavath"

    # Printing local variable
    print("Local Name:", name)

# Calling function
show()

# Printing global variable
print("Global Name:", name)
