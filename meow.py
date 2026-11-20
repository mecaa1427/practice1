def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b 

def divide(a, b):
    if b == 0:
        return "error cannot divide by zero"

num1 =int(input("enter first number to add: "))
num2 =int(input("enter second number to add:"))

print ("the result is  ", add(num1, num2))

sub =sub(num1, num2)

multiply =multiply(num1, num2)

divide =divide(num1, num2)

print("the result of substraction is:", sub)
print("the result of multiplication is:" , multiply)
print("the result of division is",divide)