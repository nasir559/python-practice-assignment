name = input("Enter your name: ")
age = int(input("Enter your age: "))

print()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

print()

print(f"Name: {name}")
print(f"Age: {age}")

print()

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
