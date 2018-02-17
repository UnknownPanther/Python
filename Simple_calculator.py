# | Calculator | 
# My very first program I have ever created
# You can find Original Source here-> https://www.programiz.com/python-programming/examples/calculator
# Code made in | 17.02.2018 | (1)

# This function adds two numbers
def add(x,  y):
    return x + y

# This function substracts two numbers
def subtract(x,  y):
    return x - y

# This function multiplies two numbers
def divide(x,  y):
    return x / y

print("PLease select operation.")
print("1. Add      | +")
print("2. Subtract | -")
print("3. Multiply | *")
print("4. Divide   | /")

choice = input("Enter your choice by typing |1|2|3|4|:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))
    
