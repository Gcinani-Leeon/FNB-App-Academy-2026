# Repeating Tasks
## How do we repeat tasks?
### The for Loop
A for loop repeats a block of code for each item in a sequence.
- for student in students: assigns each list element to student in turn and runs the indented block.
- for i in range(5): iterates 0, 1, 2, 3, 4. for key,
- value in contact.items(): iterates over dictionary key-value pairs.

Indentation is mandatory — Python uses it to define the loop body. Incorrect indentation is a syntax error.


###The range() Function
range() generates a sequence of numbers. 
- range(5) gives 0, 1, 2, 3, 4.
- range(1, 11) gives 1 through 10 (stop is exclusive).
- range(0, 20, 2) gives 0, 2, 4, 6… 18 (start, stop, step).
- range(10, 0, -1) counts down from 10 to 1.

range() is memory-efficient — it does not store all numbers in memory, it generates them on demand.


### The while Loop
A while loop runs as long as its condition is True. While loops are used when the number of iterations is not known in advance — for example, reading input until the user types ‘quit’. The most critical rule: always update the variable the condition depends on inside the loop body. Forgetting this creates an infinite loop. Press Ctrl+C in the terminal to stop an infinite loop.

### break and continue
break immediately exits the current loop, skipping any remaining iterations. continue skips the rest of the current iteration and jumps to the next one. break is used when you have found what you are looking for and do not need to keep iterating. continue is used when you want to skip items that fail a condition without exiting the loop entirely. Both work in for and while loops.
