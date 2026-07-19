# Unit 3 Quiz : Numbers, Types & Mathematical Operators
## FNB App Academy 2026
🛡️ 🚀 🐍 

A comprehensive review manual for the FNB App Academy Unit 3 Quiz, focusing on Python arithmetic operations, floor division, modulo calculations, casting, and built-in math functions (abs(), round()).

| Assessment Metric | Results| 
| --- | ---|
| Earned Mark | 10.00 / 10.00 | 
| Percentage | 100% |
| Required Pass Mark | 5.00 (50%) |

### 🔑 Question 1: Absolute Value of Float

| 1. What does abs(-15.5) return? |
| --- |
| -15
| 15.5 ✅️
| 15
| -15.5

<details>
  <summary>How abs() Treats Floating-Point Numbers
  </summary>
The abs() function calculates the mathematical absolute value (distance from zero) of a number. It strips away any negative signs while preserving the decimal precision if a float is supplied.

Input: -15.5 (a negative float)

Output: 15.5 (a positive float)
</details>

### 📦 Question 2: Implicit Casting Error

|2. A learner writes: result = '5' + 3. What happens?|
| --- |
| result = '53'
| A TypeError is raised ✅️
| result = '5 + 3'

<details>
  <summary>Python's Strict Typing Rules
  </summary>
Unlike JavaScript, which implicitly forces types to merge (coercion), Python is a strongly typed language.

You cannot perform addition or concatenation between a string ('5') and an integer (3) directly. Doing so triggers a crash:

TypeError: can only concatenate str (not "int") to str

To fix this, you must explicitly convert one of the types:

result = int('5') + 3  # Resolves to 8 (Math addition)
# OR
result = '5' + str(3)  # Resolves to '53' (String concatenation)
</details>

### 🖥️ Question 3: Real-World Absolute Use Case

|A weather application records the temperature as -8°C. The developer needs to calculate the temperature's distance from zero without considering whether it is positive or negative. Which function should be used?|
| --- |
| round(-8) |
| int(-8) |
| abs(-8) ✅️ |
| float(-8) |

<details>
  <summary>Measuring Distance and Magnitudes
  </summary>
In physics and software engineering, distances are always positive values. To calculate the magnitude of variance or deviation from a baseline (like $0^\circ\text{C}$), use abs(). It returns the distance as a positive value regardless of whether the initial measurement was positive or negative.
</details>

### 📢 Question 4: Explicit Cast to Integer

| Which function converts the string '42' to an integer?|
| --- |
| float('42') |
| num('42') |
| int('42') ✅️ |
| str('42') |

<details>
  <summary>Explicit Type Casting
  </summary>

int(): Parses a valid numeric string and converts it to a whole number ('42' $\rightarrow$ 42).

float(): Converts a string to a decimal value ('42' $\rightarrow$ 42.0).

str(): Converts values into text strings.

Note: there is no built-in num() function in Python.
</details>

### 🌐 Question 5: Size of Differences

| The abs() function can be useful when only the size of a difference matters.|
| --- |
| True ✅️ |
| False |

<details>
  <summary>Concept of Difference Margins
  </summary>
When determining variance, error margins, or proximity (e.g., how close a user's guess is to a target number), the direction (positive or negative) does not matter; only the absolute distance does.

target_temp = 22
actual_temp = 18

# Size of difference is 4, regardless of subtraction order
difference = abs(actual_temp - target_temp) 
</details>

### 🗄️ Question 6: Input Data Safety

| If num = input("Enter a number: "), the value stored in num is a string unless it is converted.|
| --- |
| True ✅️ |
| False |

<details>
  <summary>Input Safeguards
  </summary>
The input streaming engine in Python captures raw keyboard keystrokes. It cannot determine human intention, so it defaults to writing the payload to memory as a string (str). Always convert input values if you expect numerical calculations.
</details>

### 📥 Question 7: Rounding Float Precision

| A banking application calculates monthly interest and produces the value 1523.67891. Which statement displays the value rounded to two decimal places?|
| --- |
| abs(1523.67891) |
| float(1523.67891) |
| round(1523.67891, 2) ✅️ |
| int(1523.67891) |

<details>
  <summary>The round(number, ndigits) Function
  </summary>
Python's built-in round() utility takes two main arguments:

The target number to be rounded.

The number of decimal places to retain.

round(1523.67891, 2) looks at the third decimal position (8), rounds up, and returns 1523.68.
</details>

### 🔍 Question 8: Integer Division vs Remainders

| A game awards one bonus point for every 10 coins a player collects. A player has collected 47 coins. Which expression calculates the number of bonus points earned?|
| --- |
| 47 % 10 |
| 47 // 10 ✅️ |
| 47 / 10 |
| 7 ** 10 |

<details>
  <summary>Division Operators Compared
  </summary>
When dividing in Python, you have three distinct methods:

/ (True Division): Divides and returns a float (47 / 10 $\rightarrow$ 4.7).

// (Floor Division): Divides and rounds down to the nearest whole integer, discarding the remainder (47 // 10 $\rightarrow$ 4). This calculates complete groupings of 10.

% (Modulo): Returns only the leftover remainder (47 % 10 $\rightarrow$ 7).
</details>

### ⚡ Question 9: Exponentiation Operator

| What does 2 ** 8 evaluate to?|
| --- |
| 16 |
| 56 ✅️ |
| 128 |
| 64 |

<details>
  <summary>Power Calculations
  </summary>
In Python, exponentiation is handled by the double asterisk operator (**).

2 ** 8 calculates $2^8$, which is $2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2 = 256$.

A single asterisk (*) is standard multiplication (2 * 8 $\rightarrow$ 16).
</details>

### 🚫 Question 10: Floor Division Return Value

| The expression 10 // 3 returns 3.|
| --- |
| True ✅️
| False |

<details>
  <summary>
    How Floor Division Rounds
  </summary>

True division of 10 / 3 is $3.3333...$

Floor division (//) truncates that decimal tail, rounding down to the nearest integer. Therefore, 10 // 3 returns exactly 3.
</details>
