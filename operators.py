#Arithmetic Operations Program

def arithmetic(a,b):
    print("Addition:",a+b)
    print("Subtraction:",a-b)
    print("multiplication:",a*b)
    print("division:",a/b)
    print("modulus:",a//b)
arithmetic(5,7)    


#Increment and Decrement Program

num=int(input("enter a number:"))
num=num+1
print("After increment:",num)
num=num-1
print("After decrement:",num)


# Equal and Not Equal Operators

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if num1==num2:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")



#Relational Operators Program

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print("a<b:",a<b)
print("a<=b:",a<=b)
print("a>b:",a>b)
print("a>=b:",a>=b)

#Find Larger and Smaller Number

a=15
b=8
if a>b:
    print("Larger number is:",a)
    print("Smaller number is:",b)
else:
    print("Larger number is:",b)
    print("Smaller number is:",a)
