# Unit 5 Quiz Study 
🛡️ 🚀 🐍 

| Assessment Metric | Results |
| --- | --- |
| Earned Mark | 10.00 / 10.00 |
| Percentage | 100% |
| Required Pass Mark | 5.00 (50%) |

## Control Flow & Logical Operators


### 🔑 Question 1: Range Evaluation in Conditionals

|What is the output when mark = 72 is evaluated against: A(80+), B(70-79), C(60-69)?|
| --- |
| A |
| C |
| B ✅|
| No output — 72 does not match any range |

<details>
  <summary>Conditional Range Matching</summary>
Evaluating numerical boundaries in Python checks which boolean condition resolves to True. Since 72 is greater than or equal to 70 and less than or equal to 79, it falls directly into the B grade bracket.
</details>


### 📦 Question 2: Operator Precedence Rules

|Because logical operators are evaluated before comparison operators, brackets are always required.|
| --- |
| True |
| False ✅|

<details>
  <summary>Operator Precedence Order</summary>
In Python's execution hierarchy, comparison operators (<, >, ==, !=) are evaluated BEFORE logical operators (not, and, or).

Therefore, an expression like x > 5 and y < 10 automatically evaluates (x > 5) and (y < 10) first without requiring explicit parentheses.
</details>


### 🖥️ Question 3: Truthiness Checks

|What does if username: check?|
| --- |
| Whether username equals True |
| Whether username is not empty, None, or 0 ✅|
| Whether username is a string |
| Whether username is defined | 

<details>
  <summary>Implicit Truthiness</summary>
  Python automatically converts non-boolean variables into booleans when placed in an if statement:

Truthy Values: Non-empty strings ("Leeon"), non-zero numbers (1), non-empty collections ([1, 2]).

Falsy Values: Empty strings (""), zero (0), None, empty collections ([], {}).

if username: checks if the variable contains a truthy value (i.e. is not empty, 0, or None).
</details>



### 📢 Question 4: Fallback else Execution

|The else block is executed only when every preceding if and elif condition is False.|
| --- |
| True ✅|
| False |

<details>
  <summary>The Role of else</summary>
An else statement acts as the ultimate safety net or default branch in a conditional chain. It triggers if and only if all preceding if and elif condition checks evaluate to False.
</details>


### 🌐 Question 5: List Membership Testing

Which of the following checks if 'admin' is in the list roles?|
| roles.contains('admin')
| --- |
| 'admin' in roles ✅|
| roles == 'admin' |
| 'admin'.find(roles) |

<details>
  <summary>The in Keyword</summary>
  Python provides the clean, English-like membership operator in to check whether an item exists inside a collection.

roles = ["user", "editor", "admin"]
if "admin" in roles:
    print("Access granted!")
</details>


### 🗄️ Question 6: Versatility of in

|The in keyword can only be used with lists. |
| --- |
| True |
| False ✅|

<details>
  <summarySupported Iterable Collections></summary>
The in keyword works across virtually all Python collections and iterables, including:

Strings: 'py' in 'python' ($\rightarrow$ True)

Tuples: 1 in (1, 2, 3) ($\rightarrow$ True)

Dictionaries: Checks keys by default ('email' in contact)

Sets: 'apple' in fruit_set ($\rightarrow$ True)
</details>


📥 Question 7: Logical Negation

|The not operator changes True to False and False to True.|
| --- |
| True ✅|
|  False |

<details>
  <summary>Boolean Inversion</summary>
The not operator is a unary operator that inverts the logical state of any boolean expression:

not True $\rightarrow$ False

not False $\rightarrow$ True
</details>


### 🔍 Question 8: Empty Collection Truthiness

|An empty list is considered truthy in Python.|
| --- |
| True |
| False ✅|

<details>
  <summary>Empty Collections evaluate to False</summary>
In Python boolean evaluation, all empty containers ([], (), {}, "", set()) evaluate to False. This makes checking for empty data simple:

items = []
if not items:
    print("No items found!") # This line executes!
</details>



###⚡ Question 9: Inclusive Logical Disjunction (or)
|Using the or operator allows a condition to be True if only one condition is True.|
| --- |
| True ✅|
| False |

<details>
  <summary>How or Evaluates</summary>
The or operator requires at least one operand to be True for the overall expression to evaluate to True. It only returns False if both conditions are False.
</details>


### 🚫 Question 10: Short-Circuit Evaluation
|In an if/elif/else structure, Python evaluates every condition before deciding which block to execute.|
| --- |
| True |
| False ✅|

<details>
  <summary>Short-Circuit Mechanics</summary>
Python uses short-circuit evaluation when checking if/elif/else chains. It evaluates conditions top-to-bottom and stops immediately as soon as it finds a condition that is True, executing that block and completely skipping all remaining elif and else blocks.
</details>
