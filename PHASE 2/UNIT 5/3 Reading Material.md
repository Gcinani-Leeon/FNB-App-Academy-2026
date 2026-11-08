# Selection of Tasks

## How do we select tasks?

### Conditional Logic
Without conditional logic, every program runs the same way every time regardless of input. Conditionals (if/elif/else) let your program make decisions. Python checks each condition in order and executes the first block where the condition is True.
- elif (else-if) chains multiple conditions.
- The else block is the fallback, it runs when all other conditions are False.

Indentation is not optional, it is how Python knows which code belongs to which condition.


### Comparison Operators
Six comparison operators return True or False: 
- "==" (equal to),
- "!=" (not equal to),
- ">" (greater than),
- "<" (less than),
- ">=" (greater than or equal to),
- "<=" (less than or equal to).

 Confusing these is one of the most common bugs in beginner code.
- "=" is assignment (age = 22).
- "==" is comparison (age == 22).


### Logical Operators
Three logical operators combine conditions.
- and: both conditions must be True.
- or: at least one condition must be True.
- not: inverts the result (True becomes False, False becomes True). Example:
    - if age >= 18 and has_id: grants entry only when both conditions are met.

Logical operators are evaluated after comparison operators, no brackets needed in most cases, but they improve readability.


### The in Keyword and Truthiness
The in keyword checks membership: if ‘admin’ in roles checks whether ‘admin’ is in the roles list. It works on strings too: if ‘@’ in email checks for a valid email format. Python also has a concept of truthiness , empty strings, 0, None, and empty lists are all falsy. This means if username: is a valid check for whether a string is non-empty.
