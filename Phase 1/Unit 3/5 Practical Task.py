# calculator.py 

# Multi-Function Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

Addition = num1 + num2
Subtraction = num1 - num2
Multiplication = num1 * num2
Division = num1 / num2
Floor_Division = num1 // num2
Modulus = num1 % num2

print("Addition : num1 + num2 = " + str(Addition))
print("Subtraction : num1 - num2 = " + str(Subtraction))
print("Multiplication : num1 * num2 = " +str(Multiplication))
print("Division : num1 / num2 = " + str(Division))

print("floor Division : num1 // num2 = " + str(num1 // num2))
print("Modulus : num1 % num2 = " + str(num1 % num2))