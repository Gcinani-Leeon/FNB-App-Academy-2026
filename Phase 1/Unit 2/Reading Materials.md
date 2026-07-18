# Manipulating Strings
 

## Why strings matter?
Strings are the most common data type in app development. Every piece of text your app displays ; usernames, messages, button labels, error messages, search results is a string. Python gives you a rich set of built-in methods for transforming, searching, and formatting string data. Mastering these tools means you can shape user input into exactly the form your app needs.

## String Methods
A method is a built-in function that belongs to a specific data type. You call it using dot notation:
- variable.method().

Key string methods: 
- .upper() converts to ALL CAPS
- .lower() converts to all lowercase;
- .title() converts to Title Case;
- .strip() removes leading and trailing whitespace;
- .replace(old, new) swaps one substring for another;
- .find(substring) returns the index of the first occurrence (-1 if not found);
- .split(delimiter) breaks a string into a list;
- len(string) returns the character count.

## Indexing and Slicing
Every character in a string has a position number called an index, starting at 0.
- name = ‘Python’
  
- name[0]  #gives ‘P’,
- name[1] #gives ‘y’,
- name[-1] #gives ‘n’ (the last character).

Slicing extracts a portion
- name[0:3] #gives ‘Pyt’ (from index 0 up to but not including index 3).

Negative indexes count from the right:
- name[-3:] gives ‘hon’.

## f-strings
An f-string (formatted string literal) is the cleanest way to embed variables and expressions inside text. Prefix the string with f, then wrap any variable or expression in curly braces: 
- f’Welcome, {name.title()}!’.

You can call methods, do arithmetic, and embed any Python expression inside the curly braces. f-strings replace older methods like .format() and % formatting and are the preferred style in modern Python.
