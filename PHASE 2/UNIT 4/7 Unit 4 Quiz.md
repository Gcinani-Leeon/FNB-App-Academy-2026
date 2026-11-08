# Unit 4 Quiz

🛡️ 🚀 🐍 

| Assessment Metric | Results |
| --- | --- |
| Earned Mark | 10.00 / 10.00
| Required Pass Mark | 5.00 (50%) | 

## Data Storage & Retrieval Structures

### 🔑 Question 1: Read-Only Storage Choice

| If data should never change, a tuple is generally a better choice than a list. |
| --- |
| True ✅️|
| False |

<details>
  <summary>Why Choose Immutable Collections?</summary>
A Tuple is functionally identical to a List, except it is strictly read-only (immutable). Once created, you cannot append, pop, change, or rearrange its contents.

Utilizing tuples for critical system variables (such as GPS coordinates, UI RGB color configurations, or days of the week) guarantees that other parts of your code cannot accidentally overwrite, modify, or corrupt your data.

# Modifying a tuple triggers a TypeError
coordinates = (26.2, 28.0)
try:
    coordinates[0] = 30.5
except TypeError as e:
    print(f"Error: {e}")  # Output: 'tuple' object does not support item assignment
</details>


### 📦 Question 2: Crash Prevention in Dictionaries

|Using contact.get("email") is a safer way to retrieve a value than contact["email"] when the key might not exist.|
| --- |
| True ✅️|
| False |


<details>
  <summary>Bracket Lookup vs Safe Retrieval</summary>

Direct Bracket Access (contact['email']): If the key is missing from the dictionary, Python immediately crashes the program with a fatal KeyError.

Safe Access (contact.get('email')): If the key is missing, Python returns None (or a fallback value you define) instead of crashing your application.

contact = {"name": "Amara"}

# print(contact["email"])     # ❌ Crashes with KeyError!
print(contact.get("email"))   # ✅ Safe! Returns: None

</details>

🖥️ Question 3: Missing Key Return Values

|What does contact.get('email') return if 'email' is not a key in the dictionary?|
| --- |
| An empty string |
| false |
| A KeyError |
| none (Python's native None) ✅️|


<details>
  <summary>Understanding None</summary>
By default, the .get() method returns Python's native placeholder for "nothing" (None). You can also configure .get() to return a specific default string if you want to provide fallback info:

print(contact.get("email", "Email not registered")) # Custom fallback
</details>


📢 Question 4: Negative Index Navigation

|If students = ["Amara", "Sipho", "Lerato"], then students[-1] returns "Lerato".|
| --- |
| True |
| False ✅️|


<details>
  <summary>Counting backwards from the end</summary>
Negative indexes act as a shortcut to read collections from right-to-left:

students[-1] gets the last element ("Lerato").

students[-2] gets the second-to-last element ("Sipho").
</details>

🌐 Question 5: Modifying Lists

|Which method adds an item to the END of a list?|
| --- |
| .insert() |
| .add() |
| .append() ✅️|
| .push() |


<details>
  <summary>Appending to Lists</summary>

.append(value): Squeezes the new item directly onto the tail of the list.

.insert(index, value): Inserts an item at a specific index position, pushing later items to the right.
</details>

🗄️ Question 6: Looping Over Complex Structures

|A learner iterates: for contact in contacts:. Inside the loop, how do they access the contact's phone number if the key is 'phone'?|
| --- |
| contact.phon |
| contacts['phone'] |
| contact['phone'] ✅️|
| phone(contact) |


<details>
  <summary>Reading List of Dictionaries</summary>
In a loop over contacts (which is a list of dictionaries), the temporary loop variable contact holds one individual dictionary record at a time. Therefore, you query that individual record directly using standard bracket syntax: contact['phone'].

contacts = [
    {"name": "Amara", "phone": "071 234 5678"},
    {"name": "Sipho", "phone": "082 111 2222"}
]

for contact in contacts:
    print(contact['phone']) # Prints individual phone numbers
</details>


📥 Question 7: Accessing Keys

|How do you access the value for key 'name' in the dictionary person = {'name': 'Sipho', 'age': 22}?|
| --- |
| person.name |
| person[0]
| person['name'] ✅️|
| person.get(name) |


<details>
  <summary>Dictionary Query Syntax</summary>
Dictionaries are unordered and cannot be queried by numerical indexes (like person[0]). You must use the string key literal wrapped in brackets: person['name'].

Note on person.get(name): This is a trap! It looks for a variable named name which doesn't exist, leading to a NameError. It would need quotes: person.get('name').
</details>

🔍 Question 8: Count Functions

|What is the output of: len(['a', 'b', 'c', 'd'])?|
| --- |
| 3 |
| 4 ✅️|
| 'd' |
| 0 |


<details>
  <summary>Counting Items</summary>
The len() function evaluates the length/size of any collection. Since there are 4 individual elements in the array, the output is 4.
</details>

⚡ Question 9: List Creation Syntax

|Which of the following correctly creates a list of students?|
| --- |
| students = ('Amara', 'Sipho', 'Lerato') |
| students = ['Amara', 'Sipho', 'Lerato'] ✅️|
| students = {'Amara', 'Sipho', 'Lerato'} |
| students = |


<details>
  <summary>Bracket Standard Comparison</summary>

[ ... ] (Square Brackets): Creates a List (ordered, mutable).

( ... ) (Parentheses): Creates a Tuple (ordered, immutable).

{ ... } (Curly Brackets): Creates a Set (unordered, unique) or a Dictionary if it contains colons (key: value).
</details>

🚫 Question 10: Understanding Mutability

|Why are lists considered mutable? |
| --- |
| They cannot be changed |
| They can be modified after creation ✅️|
| They store key-value pairs |
| They are immutable like tuples |


<details>
  <summary>What is Mutability?</summary>
In computer science, mutable means "changeable". Lists are mutable because you can update elements, append new ones, sort the sequence, or delete items directly in memory without having to destroy and recreate the container itself.
</details>
