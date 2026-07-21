# Unit 6 Quiz Study

🛡️ 🚀 🐍 

A comprehensive review manual for the FNB App Academy Unit 6 Quiz, focusing on Python loop structures (for and while), sequence generation with range(), iteration controls (break and continue), and loop target variables.

|Assessment MetricResults|
| --- |
|Earned Mark | 10.00 / 10.00|
|Percentage | 100%|
|Required Pass Mark | 5.00 (50%)|

### 🔑 Question 1: Nature of for Loops
|A for loop repeats a block of code once for every item in a sequence.|
| --- |
| True X |
| False |

<details>
  <summary>Definite Iteration</summary>
In Python, a for loop performs definite iteration. It processes elements sequentially across an iterable collection (such as a list, string, tuple, or range). It automatically terminates once every item in the sequence has been processed.
</details>

📦 Question 2: Infinite while Loops

| What causes an infinite while loop? |
| --- |
| Using while True: |
| [x] Not updating the variable the condition depends on |
| Having too many items in the list |
|  Using break inside the loop |

<details>
  <summary>Loop State Mutation</summary>
A while loop continues executing as long as its conditional evaluation remains True. If the loop body fails to modify or update the state variables involved in that condition, the condition will never become False, locking the application into an infinite loop.

count = 1

while count <= 5:

    print(count)
    
    # If we omit `count += 1`, this loop runs forever!
    
    count += 1

</details>

🖥️ Question 3: break vs. continue

| The break statement skips the current iteration and continues with the next one. |
| --- |
| True |
| [x] False |

<details>
  <summary>Terminating vs. Skipping</summary>

break: Immediately aborts the entire loop, jumping program execution to the first line after the loop block.

continue: Skips only the remainder of the current iteration pass and jumps directly to the start of the next pass.
</details>

📢 Question 4: Step Slicing in range()

|What does range(2, 10, 3) generate? |
| --- |
| [x] 2, 5, 8 |
| 2, 3, 4, 5, 6, 7, 8, 9 |
| 2, 5, 8, 11 |
| 3, 6, 9 |

<details>
  <summary>more</summary>
The range(start, stop, step) Utility

start = 2 (inclusive initial value)

stop = 10 (exclusive upper bound)

step = 3 (increment amount per step)

Progression: $2 \rightarrow 2+3=5 \rightarrow 5+3=8 \rightarrow 8+3=11$ (11 reaches/exceeds boundary 10, so it stops).
Result sequence: 2, 5, 8.
</details>

🌐 Question 5: Loop Termination via break

|What does the break statement do inside a loop? |
| --- |
| Skips the current iteration and continues to the next|
[x] Exits the loop immediately |
| Pauses the loop for 1 second |
| Restarts the loop from the beginning |

<details>
  <summary>Immediate Abort Boundary</summary>
When a break statement is encountered during execution, Python bypasses all remaining lines inside that loop pass and breaks out of the loop block entirely, handing control back to the outer script context.
</details>

🗄️ Question 6: Selective Filtering with continue
|The continue statement allows a loop to skip items that fail a condition without terminating the entire loop.|
| --- |
| [x] True |
| False |

<details>
  <summary>Bypassing Unwanted Data</summary>
continue is useful for input validation or filtering out unwanted records. If a condition is met (e.g., encountering invalid data), continue skips processing for that specific item and proceeds to the next record in the loop sequence.
</details>

📥 Question 7: Sentinel Event Loop Pattern

|A learner needs to loop until the user types 'quit'. Which structure is most appropriate? |
| --- |
| for i in range(999): |
| [x] while True: with break when input == 'quit' |
| if input == 'quit': |
| for input in users: |

<details>
  <summary>Indefinite Interactive Loops</summary>
When you cannot predict how many times a user will interact with a terminal interface before exiting, an indefinite loop structure (while True:) paired with a conditional break statement on user input (a "sentinel value") is the standard pattern.
</details>

while True:
    user_action = input("Enter command: ")
    if user_action == "quit":
        break


🔍 Question 8: Default Zero-Indexing in range()

|What is the output of: for i in range(3): print(i)? |
| --- |
| 1 2 3 |
| 0 1 2 3 |
| [x] 0 1 2 |
| 1 2 |

<details>
  <summary>Default Bounds of Single-Argument range(n)</summary>
When range() is called with a single argument n:

The default start value is 0.

The stop limit is n (exclusive).

range(3) yields 0, 1, and 2 across three iteration cycles.
</details>

⚡ Question 9: Loop Variable Scope

|In the statement for student in students:, the variable student stores every element in the list at the same time. |
| --- |
| True |
| [x] False |

<details>
  <summary>Iteration Target Assignment</summary>
During each pass of a for loop, the loop variable (student) holds one single item from the iterable collection (students). Once the current iteration pass completes, the variable is overwritten with the next single element from the list.
</details>
🚫 Question 10: Skipping Specific Iterations

|A programmer wants to process every number from 1 to 10 except the number 5. Which statement should be used when the loop reaches 5? |
| --- |
| break |
| [x] continue |
| pass |
| stop |

<details>
  <summary>Excluding Particular Iterations</summary>

Using break when reaching $5$ would stop the loop early, preventing $6, 7, 8, 9, 10$ from being processed.

Using continue skips the processing code only for $5$, while allowing the loop to continue smoothly for $6$ through $10$.
</details>
