## Unit 2 Quiz Study Guide
### FNB App Academy 2026

🛡️ 🚀 🐍 

A complete revision manual for the FNB App Academy Unit 2 Quiz, covering python string methods, index slicing, negative values, and length calculations. Designed to look exceptional in markdown viewers, GitHub pages, and mobile displays.

|Assessment Metric | Results |
| --- | --- |
| Earned Mark | 10.00 / 10.00 |
| Percentage | 100% |
| Required Pass Mark | 5.00 (50%) |


### 🔑 Question 1: f-String Printing Syntax

| Which code correctly displays a person's name using an f-string? |
| --- |
| print(\"Welcome {name}\") |
| print(f\"Welcome, {name}\") ✅️|
| print(\"Welcome,\" + {name}) |
| print(f{Welcome, name}) |


<details>
  <summary>f-String Formatting Rules</summary>
  
To format strings cleanly in Python, you prefix the string literal with an f (or F) directly before the opening quote.

Inside the string, you place variables or expressions inside curly braces {}. The interpreter evaluates the content inside the braces on the fly and converts it to text.

Standard Syntax e.g:

name = "Leeon"

print(f"Welcome, {name}") 

Outputs ✅️🔥:
- Welcome, Leeon

</details>


### 📦 Question 2: Negative Indexing Boundary

| If word = "Python", then word[-1] returns "P".|
|-|
| True |
| False ✅️|

<details>
<summary>
  Forward vs. Negative Indexing</summary>
Python allows positive indexing (starting from the left at 0) and negative indexing (starting from the right at -1).

For the string "Python":

| Character | P | y |t |h | o |n
|---|---|---|---|---|---|---|
| Positive Index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative Index | -6 | -5 |-4 | -3| -2 | -1 |

Therefore, word[-1] resolves to the last letter, "n". To get "P", you would need word[0] or word[-6].
</details>


### 🖥️ Question 3: Dynamic Expressions inside f-Strings

|An f-string allows variables and expressions to be inserted directly into a string|
| - |
| True ✅️|
| False|

<details>
<summary>Power of Expressions</summary>

f-strings aren't limited to just pulling raw variable values. You can run code, execute calculations, and invoke method calls directly inside the curly brackets {}:
- price = 100

Math execution inside the string
- print(f"Price with tax: {price * 1.15}") 
</details>

### 📢 Question 4: String Slicing Bounds

| What does 'Python'[1:4] return? |
| - |
| 'yth' ✅️|
| 'ythn' |
| 'Pyt' |
| 'ytho' |

<details>
<summary>
The [start:stop] Slicing Rule</summary>

When slicing sequences in Python with notation [start:stop]:
- The start index is inclusive (we keep it).
- The stop index is exclusive (we stop right before it).

Slicing 'Python'[1:4] pulls indices 1, 2, and 3. It excludes index 4.
- Index 1 = 'y'
- Index 2 = 't'
- Index 3 = 'h'
- Index 4 = 'o' (Excluded)
- Result: 'yth'
</details>

### 🌐 Question 5:
Finding String Length

| What is returned by the expression len("Python")? |
|---|
| 5 |
| 6 ✅️|
| 7 |
| 8 |

<details>
<summary>
len() vs Indexes</summary>
The len() function returns the total number of characters in a string. It is a standard, 1-based count.

While the maximum positive index of "Python" is 5 (due to starting at 0), the total character count is 6.
</details>

### 🗄️ Question 6: Initial Index Rule

|What is the index of the first character in a Python string?|
|---|
| -1 |
| 0 ✅️|
| 1 |
| 10 |

<details>
<summary>
Zero-Based Indexing</summary>
Almost all modern programming languages (including Python, JavaScript, Java, and C++) use zero-based indexing. Sequences, lists, and collections always start index counts at 0.
</details>

### 📥 Question 7: String Searching Behavior

|If city = "Cape Town", then city.find("z") returns -1 because the character is not found|
| --- |
| True ✅️|
| False |

<details>
<summary>Understanding .find() Returns</summary>

The .find(substring) method searches a string for a specified value:

If the value is found, it returns the start index position of that value.

If the value is not found, it returns -1. It does not raise an execution crash, unlike the .index() method which throws a ValueError.
</details>

🔍 Question 8: Lowercase vs Uppercase

|Which string method converts all letters in a string to uppercase?|
| - |
| .title() |
| .upper() ✅️ |
| .lower() |
| .capitalize() |

<details>
<summary>
Case Modification Methods</summary>

.upper(): Converts all characters to uppercase 
- ("python" $\rightarrow$ "PYTHON").

.lower(): Converts all characters to lowercase 
- ("PyThOn" $\rightarrow$ "python").

.title(): Capitalizes the first letter of every word 
- ("cape town" $\rightarrow$ "Cape Town").

.capitalize(): Capitalizes only the first letter of the first word
- ("cape town" $\rightarrow$ "Cape town").
</details>

### ⚡ Question 9: Splitting Text into Lists

|A learner wants to split the string 'apple,banana,mango' into a list. Which is correct?|
| - |
| split('apple,banana,mango', ',') |
| 'apple,banana,mango'.split() |
| 'apple,banana,mango'.divide(',') |
| 'apple,banana,mango'.split(',') ✅️|

<details>
<summary>
Using the .split() Method</summary>

Strings are objects in Python, meaning functions are called on them using dot-notation.

The .split(separator) method takes a delimiter as its argument and cuts the string up at those points, returning a list.

string.split(',') splits on comma delimiters.

Calling .split() with no argument defaults to splitting on whitespace.
</details>

### 🚫 Question 10: Cleaning Text with .strip()

|What value is stored in username after the code below?|
|-|
| username = " Lerato " |
| username = username.strip() |
|choose below|
| \" Lerato \" |
| \"Lerato \" |
| \" Lerato\" |
| \"Lerato\" ✅️|

<details>
<summary>How .strip() Operates</summary>

.strip() removes all whitespace (spaces, tabs, newlines) from both the left and right ends of a string.

" Lerato " has a leading space and a trailing space. Stripping it returns "Lerato" with no extra spacing.

If you want to strip only one side, you can use .lstrip() (left-only) or .rstrip() (right-only).
</details>
