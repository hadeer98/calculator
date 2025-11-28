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

print("Simple Calculator")
print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")

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
else:
    print("Invalid choice")
