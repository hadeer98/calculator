import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

def power(a, b):
    return a ** b

def percent(a, b):
    return (a / b) * 100
 

def sqrt_num(a):
    return math.sqrt(a)

def modulus(a, b):
    return a % b

def maximum(a, b):
    return max(a, b)
def average(a, b):
    return (a + b) / 2
    
print("Simple Calculator")
print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")
print("5) Power")
print("6) Percent (a is what percent of b)")
print("7) Square Root")
print("8) Modulus (a % b)")
print("9) Maximum of two numbers")
print("10) Average of two numbers")
choice = input("Choose (1/2/3/4): ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if choice == "1":
    print("Result:", add(x, y))
elif choice == "2":
    print("Result:", sub(x, y))
elif choice == "3":
    print("Result:", mul(x, y))
elif choice == "4":
    print("Result:", div(x, y))
elif choice == "5":
    print("Result:", power(x, y))
elif choice == "6":
    print("Result:", percent(x, y))

elif choice == "7":
    x = float(input("Enter the number: "))
    print("Result:", sqrt_num(x))

elif choice == "8":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Result:", modulus(x, y))
elif choice == "9":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Result:", maximum(x, y))
elif choice == "10":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Result:", average(x, y))
else:
    print("Invalid choice")
