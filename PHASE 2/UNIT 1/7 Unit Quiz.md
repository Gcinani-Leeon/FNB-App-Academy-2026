# Quiz Summary
​A complete 10/10 masterclass recap! This study guide preserves the exact questions from the Unit 1 Quiz while expanding on the explanations to make them highly scannable, deeply intuitive, and perfect for quick revision before your exams.

| Passed | 100% |
| --- | ---|
| Pass Mark | 5.00 (50) |
| Earned Mark | 100.00(100%) |
| Attempted on | 16 July 2026 |


### Question 1 / 10

| 1. Which of the following best describes a dictionary? |
| --- |
| Ordered collection |
| Lookup table  ✅️|
| Immutable sequence|
| List of lists |

<details>
<summary>What is a Dictionary?</summary>

- In Python, a dictionary (dict) stores data in key-value pairs. It functions exactly like a real-world vocabulary dictionary: you look up a "word" (the key) to immediately find its "definition" (the value).

- Because you use the unique key to instantly grab the matching value without scanning the entire dataset, it operates as an efficient lookup table. 
</details>

--- 

### Question | 2/10
| 2. A variable can store different types of values, such as text, numbers, and Boolean values |
| --- |
| True ✅️|
| False |

<details>
<summary>Variables as Dynamic Containers</summary>

Think of a variable as a labeled container in memory. Because Python is dynamically typed, you do not have to explicitly state what type of data the variable holds when you create it.

You can drop any primitive data type into it freely, and even change it on the fly:

- Text String (str): name = "Leeon"
- Integer (int): age = 21
- Boolean (bool): is_studying = True
</details>

---

### Question 3/10
| 3. Which file name would VS Code recognize as a Python script? |
| --- |
| program.txt |
| program.docx |
| program.py ✅️ |
| program.exe |

<details>
  <summary>Understanding File Extensions</summary>
File extensions tell your operating system and code editor how to parse the contents of a file.

.py: Tells VS Code that this is executable Python code, triggering features like code linting, IntelliSense, and the debugger.

.txt: Plain, unexecutable text.

.docx: Rich-formatted Microsoft Word document.

.exe: A compiled machine executable
</details>​

---

### Question 4/10
| 4. The statement print("Hello, World!") allows a user to enter information into a program. |
| --- |
| True |
| False ✅️|

<details>
  <summary>Data Flow Direction</summary>

print() is strictly an Output operation. It sends information out from your program's memory to the screen.

input() is the Input operation. It halts the execution of your program and waits for the user to key in data from the terminal.
</details>

---

### Question 5/10
| Which Python structure is most similar to JSON API responses? |
| --- |
| Tuples |
| Lists of dictionaries ✅️|
| Sets |
| String |

<details>
  <summary>Mapping Python to JSON APIs</summary>
In web development, APIs send data over the network formatted as JSON (JavaScript Object Notation).

Python data structures correspond directly with JSON:

JSON Objects {} $\rightarrow$ Python Dictionaries {"key": "value"}

JSON Arrays [] $\rightarrow$ Python Lists [item1, item2]

Therefore, a standard multi-record data transmission from an API resolves directly as a List of Dictionaries in Python.
</details>


### Question 6/6
| What does each dictionary in a list of dictionaries represent? |
| --- |
| A single record ✅️|
| A list of values |
| A tuple |
| A key-value pair only |

<details>
  <summary>Tabular Analogy</summary>
When dealing with arrays of structured data, think of a spreadsheet:

- The Entire List represents the whole table.

Each Dictionary represents an individual row in that table, containing the dataset for a single record (like one individual profile or transaction).
</details>

### Question 7/10
| A learner writes: age = input('Enter age: '). What data type is stored in age? |
| --- |
| int |
| float |
| str ✅️|
| bool |

<details>
<summary>Handling User Keystrokes</summary>
The input() function grabs key inputs from the terminal. Because the computer doesn't initially know if a key sequence is meant to be text, a float, or an integer, it defaults to storing it as a text string (str).

If you type 21 into the input above, it will be stored as "21" (with quotes). To turn it into a mathematical integer, you must explicitly cast it:

age = int(input("Enter age: "))  # Successfully cast string to int
</details>

### Question 8/10
| If name = "Amara", then type(name) returns str. |
| --- |
| True ✅️|
| False |

<details>
  <summary>The type() Function</summary>
Any text enclosed in single (') or double (") quotes is explicitly identified as a string literal. When you feed that variable name into the built-in type() helper, Python confirms its data category by returning <class 'str'>.
</details>

### Question 9/10
| Why are lists of dictionaries powerful? |
| --- |
| They prevent iteration |
| They mimic database query results and API responses ✅️|
| They replace tuples |
| They store immutable values |

<details>
  <summary>The Backbone of Web Architecture</summary>
Database engines organize query results as collections of records. To bridge the database layer with your application's user interface, backends automatically parse database records into a list of dictionaries.

Because this structure easily handles loops (iteration) and holds highly flexible data, it is the absolute industry standard for building modern dynamic web pages.
</details>

### Question 10/10
| The value True is stored as a string because it contains letters. |
| --- |
| True |
| False ✅️|

<details>
<summary>Boolean Values vs String Literals</summary>

True / False (without quotes, first letter capitalized) are native Python keywords belonging to the Boolean (bool) class. They represent logical states.

If you write "True" (wrapped in quotation marks), Python treats it as a standard text string (str) and strips it of its logic capabilities.
</details>

## The End
