# Storage and Access

How do we store and access data?

### Lists
A list is an ordered, mutable collection of values stored in a single variable. 

Create one with square brackets: 
- students = [‘Amara’, ‘Sipho’, ‘Lerato’].

Access items by index (starting at 0): 
- students[0] gives ‘Amara’.

Negative indexes count from the end: 
- students[-1] gives ‘Lerato’.

Key list methods: 
- .append(item) adds to the end;
- .insert(index, item) inserts at a position;
- .remove(item) removes by value;
- .pop(index) removes by index and returns the item;
- len(list) returns the count.


### Dictionaries
A dictionary stores key-value pairs. Think of it as a lookup table where every piece of data has a name. 

Create one with curly braces: 
- contact = {‘name’: ‘Amara’, ‘phone’: ‘071 234 5678’}.

Access values by key: 
- contact[‘name’]. Use .get(‘key’) for safe access — it returns None instead of crashing if the key doesn’t exist.

Key methods: 
- .keys() returns all keys;
- .values() returns all values;
- .items() returns (key, value) pairs for iteration.

### Lists of Dictionaries
The most powerful data pattern in beginner Python is a list of dictionaries. Each dictionary represents one record (a contact, a student, a product), and the list holds all the records. This is exactly how database query results and API responses are structured — JSON responses from web APIs are nearly always lists of dictionaries. Iterating over this structure with a for loop lets you process every record in a few lines of code.

### Tuples: Immutable Lists
A tuple is like a list but immutable — once created, it cannot be changed. Create with parentheses: coordinates = (26.2, 28.0). 

Use tuples when the data should not change: 
- GPS coordinates,
- RGB colour values,
- days of the week.

Attempting to modify a tuple raises a TypeError.
