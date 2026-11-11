#1. how to write a function

# defining the application
def greating():
    print("hello world")
    
#calling the function by its name
# greating()

#the output shoul be: hello world

# ====================================================
# ====================================================


# 2. A funtion with paremeters
# Defining the Function with parameters
def vat_calculator(amount):
    vat = amount * 0.15
    print(f"The VAT for the Amount of R{amount} is R{vat}")

# Calling the function with a parameter
# vat_calculator(100)
# vat_calculator(250)

# Its recommended to round the output into 2 decimal places.

# ====================================================
# ====================================================


# 3. Retun Key-Word
# Defining the Function with parameters
def add_numbers(num1, num2):
    total = num1 + num2
    return total

# Calling the function and storing the result
total_even = add_numbers(10, 20)
total_odd = add_numbers(15, 25)

print(total_even)
print(total_odd)