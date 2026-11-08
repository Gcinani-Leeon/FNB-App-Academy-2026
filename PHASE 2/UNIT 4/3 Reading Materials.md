# Storage and Access

How do we store and access data?

### 1. Python Lists
A list is an ordered, mutable collection of values stored in a single variable. 

Create one with square brackets: 
- students = [‘Amara’, ‘Sipho’, ‘Lerato’]
- new_students = ['John', 'Amanda']

Access items by index (starting at 0): 
- print(students[0]) gives [‘Amara’].
- print(students[0:2] => ["Amara", "Sipho"]
- print(students[-1]) gives ‘Lerato’ : Negative indexes count from the end

Key list methods:
1. len(students) returns the count == 3.
2. students.append("Leeon") adds to the end;

<details>
  <summary>3. insert() and extend()</summary>
insert put tems or anothet list at a specified position;
  
students.insert(0, "Sino")  =>  insert new item
- print(students)  =>  [‘Sino’, ‘Amara’, ‘Sipho’, ‘Lerato’]

- students.insert(0, "new_students") //this will put list within another list
- print(students) =>  [[‘John’, ‘Amanda’], ‘Sino’, ‘Amara’, ‘Sipho’, ‘Lerato’]

print(student[0])  //the first item in the list is now a list
- output [‘John’, ‘Amanda’]  

4. students.extend(list)
</details>

5. students.remove(item) removes by value;
6. students.pop(index) removes by index and returns the item;
7. students.reverse() print list in reverse
8. students.sort() sort list in Alp or Numeric  order

<details>
  <summary>9. sorted()</summary>
  takes the original list and sort it in Alphabetical or Numerical order.

  sorted_students = sorted(students)
  - print(sorted_students)  =>  ‘Amara’, ‘Lerato’, ‘Sipho’ 
</details>

### 2. Dictionaries
A dictionary stores key-value pairs. Think of it as a lookup table where every piece of data has a name. 

Create one with curly braces: 
- contact = {‘name’: ‘Amara’, ‘phone’: ‘071 234 5678’}.

Access values by key: 
- contact[‘name’]. Use .get(‘key’) for safe access — it returns None instead of crashing if the key doesn’t exist.
<details>
  <summary>
    examples
  </summary>
  
Safe Access with .get()
- Direct Access: Using contact['address'] on a key that doesn't exist will crash your program with a KeyError.
- Safe Access: Using contact.get('address') returns None (or a fallback value) instead of crashing!
  
  | Crashing  ❌ OR Safe ✅| Output |
  | --- | --- |
  | print(contact['address']) | # ❌ CRASHES with KeyError |
  | print(contact.get('address')) | # ✅ Safe! Prints: None |
  | ✅ Safe! Prints: None | # 'Not Found')) # ✅ Prints: Not Found |
</details>

Key methods: 
- .keys() returns all keys;
- .values() returns all values;
- .items() returns (key, value) pairs for iteration.

### 3. Lists of Dictionaries
The most powerful data pattern in beginner Python is a list of dictionaries. Each dictionary represents one record (a contact, a student, a product), and the list holds all the records. This is exactly how database query results and API responses are structured — JSON responses from web APIs are nearly always lists of dictionaries. Iterating over this structure with a for loop lets you process every record in a few lines of code.

### 4. Tuples: Immutable Lists
A tuple is like a list but immutable — once created, it cannot be changed. Create with parentheses: coordinates = (26.2, 28.0). 

Use tuples when the data should not change: 
- GPS coordinates,
- RGB colour values,
- days of the week.

Attempting to modify a tuple raises a TypeError.

<details>
  <summary>Summary table</summary>
  
| Data Structure | Syntax | Ordered? | Mutable (Editable)? | Use Case |
| --- | --- | --- | --- | --- |
| List | [item1, item2] | ✅ Yes | ✅ Yes (Changeable) | Queues, shopping carts, dynamic lists |
| Tuple | (item1, item2) | ✅ Yes | ❌ No (Read-Only) | Coordinates, RGB colors, fixed settings|
| Dictionary | {"key": "value"} | ❌ No* | ✅ Yes (Changeable) | User profiles, database records, lookup tables |
</details>
