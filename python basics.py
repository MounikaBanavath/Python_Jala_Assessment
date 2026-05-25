#Program to print name using user input

name=input("Enter a name:")
print("My name is",name)


 #Single-line and Multi-line Comments

#This is a single-line comment

"""
This is a
multi-line comment
"""

print("hello everyone")

#Define variables for different data types

Name="Mounika"
Salary=28000
Btech=True
Grade='A'
Cgpa=8.59
Annual_salary=27000.5678
print("Name:",Name)
print("Salary:",Salary)
print("Btech:",Btech)
print("Grade:",Grade)
print("Cgpa:",Cgpa)
print("Annual_salary:",Annual_salary)


#Local and Global Variables

name="mounika"

def show():
    name="Banavath"
    print("Local Name:",name)
show()
print("Global Name:",name)


