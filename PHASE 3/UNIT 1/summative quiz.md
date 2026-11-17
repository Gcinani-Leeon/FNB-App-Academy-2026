### Question 1 : Which keyword lets a function reassign a module-level variable?

a. extern

b. global ✅

c. public

d. static

### Question 2 : A variable created inside a function body has what kind of scope?

a. Universal

b. Global

c. Local ✅

d. Built-in

### Question 3 : Which call below uses a keyword argument?

a. f[5]

b. 5, makes it a keyword argument.

c. f(x=5) ✅

d. f(*5)

e. f(5)

### Question 4 : What does this code print?
```
def hello():
print("hi")
print(hello())
```
a. hello

b. hi followed by None ✅

c. None

d. hi

### Question 5 : Where must parameters with default values appear in the parameter list?

a. In alphabetical order

b. First, before any others

c. Anywhere at all

d. After all parameters without defaults ✅

### Question 6 : By convention, Python function names are written in:

a. PascalCase

b. UPPERCASE

c. snake_case

d. camelCase

### Question 7 : What does this code print?
```
def total(*nums):
return sum(nums)
print(total(1, 2, 3))
```
a. 6

b. TypeError

c. 3

d. (1, 2, 3)

### Question 8 : The values you pass in when calling a function are called:

a. Parameters

b. Arguments

c. Operators

d. Attributes

### Question 9 : What does this code print?
```
def apply(fn, value):
return fn(value)
print(apply(abs, -7))
```

a. 7

b. abs

c. TypeError

d. -7

### Question 10 : What does this code print?
```
x = 10
def change():
x = 5
change()
print(x)
```

a. 10

b. None

c. 5

d. NameError

### Question 11 : What does this code print?
```
def count(**kw):
return len(kw)
print(count(a=1, b=2))
```

a. 1

b. TypeError

c. 0

d. 2


### Question 12 : What does **kwargs collect inside a function?

a. Default values only

b. Extra positional arguments, as a list

c. Extra keyword arguments, as a dictionary

d. The docstring

### Question 13 : What does this code print?
```
def sub(a, b):
return a - b
print(sub(b=2, a=10))
```

a. TypeError

b. 12

c. 8

d. -8

### Question 14 : What is the main advantage of writing functions?

a. Variables become global

b. Programs run faster automatically

c. Errors are prevented

d. Code can be reused instead of repeated

### Question 15 : Which statement is used as a placeholder for a function body you have not written yet?


a. skip

b. null

c. pass

d. empty

### Question 11 : What does this code print?
```
def count(**kw):
return len(kw)
print(count(a=1, b=2))
```

a.
1

b.
TypeError

c.
0

d.
2

### Question 12 :
What does **kwargs collect inside a function?

a.
Default values only

b.
Extra positional arguments, as a list

c.
Extra keyword arguments, as a dictionary

d.
The docstring

### Question 13 : What does this code print?
```
def sub(a, b):
return a - b
print(sub(b=2, a=10))
```

a.
TypeError

b.
12

c.
8

d.
-8

### Question 14 : What is the main advantage of writing functions?

a.
Variables become global

b.
Programs run faster automatically

c.
Errors are prevented

d.
Code can be reused instead of repeated

### Question 15 : Which statement is used as a placeholder for a function body you have not written yet?

a.
skip

b.
null

c.
pass

d.
empty

### Question 16 : How many expressions can the body of a lambda contain?

a.
Two

b.
One

c.
Any number

d.
Up to five

### Question 17 : What happens to code written after a return statement inside a function?

a.
It never runs once the return executes

b.
It causes a syntax error

c.
It always runs

d.
It runs only inside loops

### Question 18 : What does *args collect inside a function?

a.
Only the first argument

b.
The function's return value

c.
Extra keyword arguments, as a dictionary

d.
Extra positional arguments, as a tuple

### Question 19 :What is a nested function?

a.
A function with default parameters

b.
A function that calls itself

c.
A function defined inside another function

d.
A function that takes another function as an argument

### Question 20 : What does this code print?
```
def fact(n):
if n < 1:
return 1
return n * fact(n - 1)
print(fact(4))
```

a.
10

b.
24

c.
1

d.
4