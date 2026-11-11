## 1. How to Write a Function

A function is a block of code that performs a specific, defined operation whenever it is called by its name. Think of it like defining a custom recipe so you can cook it anytime without reading the cookbook every time.

***Here is an example of a function, explained below:***

```python
# Defining the function
def greeting():
    print("Hello, world!")
    
# Calling the function by its name
greeting()

# The output:
Hello, world!
```

**Defining the function**

- def: Tells Python that this block of code is a function.

**The colon (:)**

- The colon at the end of the first line of the function is mandatory, followed by indenting all lines of code that belong inside that function.

**The function block code**

- Any line of code that is not indented does not belong to the defined function, even if it appears right below it.


## 2. Parameterised Functions

A function that executes a specific task when called is very useful, but a function that takes custom information is even everything.

In this example, we are going to allow a user to enter a custom amount in Rands, and the function will calculate the VAT of that custom amount.

```python
# Defining the function with a parameter
def vat_calculator(amount):
    vat = amount * 0.15
    print(f"The VAT for the amount of R{amount} is R{vat}")

# Calling the function with arguments
vat_calculator(100)
vat_calculator(250)
```

**The explaination**

- `amount` in the function definition is a parameter because it is a placeholder with no specific value yet.

- 100 / 250 when calling the function are arguments because they provide the actual values necessary for executing the function.

Essentially, the function defines parameters and waits for argument values from the user since the final output depends on what is passed in.


## 3. The `retun` Keyword
When a function includes a return statement:

It evaluates the expression and passes the resulting value back to the place where the function was called. This allows you to store the result in a variable, pass it into another function, or use it in conditional logic.

The moment the `return` statement is executed, the function stops running immediately. Any code written inside that function after the `return` statement is considered unreachable (dead code) and will not execute.

Below is code that takes two numbers and returns their sum:

```python
# Defining the function with parameters
def add_numbers(num1, num2):
    total = num1 + num2
    return total

# Calling the function and storing the result in variables
total_even = add_numbers(10, 20)
total_odd = add_numbers(15, 25)

print(total_even)
print(total_odd)
```

Notice that when we print the total, we do not pass the actual value (argument) directly to the print statement; instead, we pass the variable. This variable now holds the actual sum value, meaning we can reuse it anywhere in our code, such as passing it into other functions without issues.
