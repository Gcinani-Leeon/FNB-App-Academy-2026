# Manipulating Numbers
 
## Arithmetic Operators
Python supports seven arithmetic operators. 
- Addition (+),
- Subtraction (-),
- Multiplication (*), and
- Division (/).

  》Division always returns a float, even for whole numbers:
  - 10/2 gives 5.0 not 5.
  
  》Floor division (//) discards the decimal:
  - 10//3 gives 3.

  》Modulus (%) returns only the remainder:
  - 10%3 gives 1.
  
  》Exponentiation (**) raises to a power:
  - 2**10 gives 1024.

### The Type Casting Gotcha
input() always returns a string. This causes a very common beginner error: if you write 
- num = input(‘Enter a number: ‘)
- and then try num + 5,
- Python will raise a TypeError because you cannot add a string and an integer.

The fix is type casting, wrapping input() with int() or float(). 
- Use int() for whole numbers
- and float() when decimals are possible.

This applies everywhere you take numeric input from a user.

### Useful Number Functions
Python has several built-in functions for working with numbers. 

round(value, n) rounds to n decimal places: 
- round(3.14159, 2) gives 3.14. 

abs(value) returns the absolute value (removes the negative sign): 
- abs(-7) gives 7.
- This is useful when you care about the magnitude of a difference, not its direction. 

int(), float(), and str() convert between types,
- these are your main type casting tools.

### Operator Precedence
Python follows standard mathematical order of operations:

brackets first 》 exponents 》 multiplication/division/modulus 》 addition/subtraction.
- 💡Memorise BEDMAS.
- When in doubt, add brackets:
- (2 + 3) * 4 = 20,

  whereas 2 + 3 * 4 = 14
  because multiplication happens before addition.
