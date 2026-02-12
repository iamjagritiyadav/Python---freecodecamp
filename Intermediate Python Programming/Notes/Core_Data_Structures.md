# CORE DATA STRUCTURES

## 1.      LISTS 

## 1.1 WHAT EXACTLY IS A LIST?

A list in Python is:

* Ordered collection
* Mutable
* Dynamic in size
* Allows duplicate elements
* Stores references to objects (not raw values)

Example:

```python
l = [1, 2, 3]
```

Important: The list does NOT store integers directly. It stores references (memory addresses) to integer objects.

Proof:

```python
x = 10
l = [x]

print(id(x))
print(id(l[0]))
```

Both IDs will be the same.

Meaning: list stores object references.

---

## 1.2 MUTABILITY – WHAT DOES IT REALLY MEAN?

Mutable means we can modify the object without changing its identity.

```python
l = [1, 2, 3]
print(id(l))

l.append(4)
print(id(l))
```

The ID remains the same.

Now compare with immutable type:

```python
s = "hello"
print(id(s))

s = s + " world"
print(id(s))
```

ID changes → new object created.

Why list is mutable?

* Designed for dynamic data storage
* Efficient in-place updates
* Avoids unnecessary object creation

---

## 1.3 INTERNAL IMPLEMENTATION (CPYTHON CONCEPT)

Python lists are implemented as dynamic arrays.

Dynamic array means:

* Continuous memory block
* Pre-allocated capacity
* Resizes when capacity exceeded

Example conceptually:

Capacity = 4
Append 5th element →

1. New larger memory block allocated
2. Old elements copied
3. Old memory released

Therefore:

* Index access → O(1)
* Append → Amortized O(1)
* Insert in middle → O(n)
* Delete from middle → O(n)

Worst-case append during resize → O(n)

---

## 1.4 ALL WAYS TO CREATE LISTS

```python
l1 = []
l2 = list()
l3 = [1, 2, 3]
l4 = list((1, 2, 3))
```

Repeated elements:

```python
l = [0] * 5
print(l)
```

Output:

```
[0, 0, 0, 0, 0]
```

---

## 1.5 DANGEROUS PITFALL – NESTED LIST REFERENCE ISSUE

Wrong way:

```python
matrix = [[0]*3] * 3
print(matrix)
```

Now modify:

```python
matrix[0][0] = 99
print(matrix)
```

Output:

```
[[99, 0, 0],
 [99, 0, 0],
 [99, 0, 0]]
```

Why?

Because all rows reference the SAME inner list.

Check:

```python
print(id(matrix[0]))
print(id(matrix[1]))
print(id(matrix[2]))
```

All IDs are identical.

Correct way:

```python
matrix = [[0]*3 for _ in range(3)]
```

Now each row has different memory address.

---

## 1.6 INDEXING – ALL CASES

```python
l = [10, 20, 30, 40]

print(l[0])     # 10
print(l[-1])    # 40
```

Invalid index:

```python
print(l[10])
```

Raises:

```
IndexError: list index out of range
```

Why?

Python checks boundary before accessing memory.

---

## 1.7 SLICING – COMPLETE BEHAVIOR

Syntax:

```python
l[start:stop:step]
```

Examples:

```python
l = [1, 2, 3, 4, 5]

print(l[1:4])
print(l[:3])
print(l[::2])
print(l[::-1])
```

Important:
Slicing creates a NEW list (shallow copy).

Proof:

```python
l = [[1], [2], [3]]
l2 = l[:]

print(id(l))
print(id(l2))

print(id(l[0]))
print(id(l2[0]))
```

Outer list different.
Inner lists same.

Meaning: slicing is shallow copy.

---

## 1.8 ADDING ELEMENTS – FULL ANALYSIS

append()

```python
l = [1, 2]
l.append(3)
print(l)
```

extend()

```python
l = [1, 2]
l.extend([3, 4])
print(l)
```

Difference:

```python
l = [1, 2]
l.append([3, 4])
print(l)
```

Output:

```
[1, 2, [3, 4]]
```

insert()

```python
l = [1, 2, 3]
l.insert(1, 99)
print(l)
```

Time Complexity:

* append → O(1) amortized
* insert → O(n)

---

## 1.9 REMOVING ELEMENTS

pop()

```python
l = [1, 2, 3]
x = l.pop()
print(x)
print(l)
```

remove()

```python
l = [1, 2, 3, 2]
l.remove(2)
print(l)
```

Removes first occurrence only.

If value not found:

```
ValueError
```

clear()

```python
l.clear()
```

---

## 1.10 SORTING – INTERNAL BEHAVIOR

```python
l = [5, 2, 8, 1]
l.sort()
print(l)
```

Uses Timsort (stable hybrid sorting algorithm).
Time complexity: O(n log n)

Custom sorting:

```python
l = [(1, 'b'), (2, 'a'), (3, 'c')]
l.sort(key=lambda x: x[1])
print(l)
```

---

## 1.11 COPYING – FULL TRUTH

Reference copy:

```python
l1 = [1, 2, 3]
l2 = l1

l2.append(4)
print(l1)
```

Both changed.

Shallow copy:

```python
l2 = l1[:]
```

Deep copy:

```python
import copy
l2 = copy.deepcopy(l1)
```

Deep copy required when nested mutable elements exist.

---

## 1.12 LIST COMPREHENSION – ADVANCED USAGE

Basic:

```python
squares = [x*x for x in range(10)]
```

With condition:

```python
evens = [x for x in range(10) if x % 2 == 0]
```

Nested:

```python
matrix = [[i*j for j in range(3)] for i in range(3)]
```

---

## 1.13 MEMBERSHIP TEST

```python
l = [1, 2, 3]
print(2 in l)
```

Time Complexity → O(n)

For faster membership → use set.

---

## 1.14 COMMON INTERVIEW TRAPS

Mutable default argument trap:

```python
def func(x=[]):
    x.append(1)
    return x

print(func())
print(func())
```

Why does it keep growing?
Because default argument evaluated once at function definition time.

Correct way:

```python
def func(x=None):
    if x is None:
        x = []
    x.append(1)
    return x
```

---

---

## 1.15 IDENTITY vs EQUALITY (is vs ==)

Equality (==) checks VALUE.
Identity (is) checks MEMORY LOCATION.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True (values same)
print(a is b)   # False (different objects)
```

Now:

```python
c = a
print(a is c)   # True
```

Rule:
Use == to compare values.
Use is only for:

* None
* Checking same object intentionally

Correct:

```python
x = None
if x is None:
    print("Correct check")
```

Never use:

```python
if x == None:   # not recommended
```

---

## 1.16 REFERENCE COUNTING AND GARBAGE COLLECTION

Every Python object has reference count.

Example:

```python
import sys

a = [1,2,3]
print(sys.getrefcount(a))

b = a
print(sys.getrefcount(a))
```

When reference count becomes zero → object eligible for garbage collection.

Example:

```python
a = [1,2,3]
b = a

del a
print(b)
```

Object not deleted because b still references it.

Now:

```python
del b
```

Now object can be garbage collected.

---

## 1.17 DEL KEYWORD – FULL BEHAVIOR

Delete element by index:

```python
l = [10,20,30]
del l[1]
print(l)
```

Delete slice:

```python
l = [1,2,3,4,5]
del l[1:4]
print(l)
```

Delete entire list:

```python
l = [1,2,3]
del l
# print(l)  -> NameError
```

Important:
del removes reference, not necessarily object immediately.

---

## 1.18 SLICE ASSIGNMENT – POWERFUL BUT DANGEROUS

You can modify multiple elements at once.

```python
l = [1,2,3,4]
l[1:3] = [99, 100]
print(l)
```

Output:
[1, 99, 100, 4]

Length can change:

```python
l = [1,2,3,4]
l[1:3] = [9]
print(l)
```

Output:
[1, 9, 4]

Replace entire list without changing identity:

```python
l = [1,2,3]
id_before = id(l)

l[:] = [10,20]

print(l)
print(id(l) == id_before)   # True
```

This modifies in-place.

---

## 1.19 LIST VS TUPLE MEMORY COMPARISON

```python
import sys

l = [1,2,3]
t = (1,2,3)

print(sys.getsizeof(l))
print(sys.getsizeof(t))
```

Tuple usually consumes less memory.

Reason:

* Tuple is immutable
* No need for dynamic resizing overhead

---

## 1.20 TIME COMPLEXITY TABLE

## Operation                 Time Complexity

Index access              O(1)
Append                    O(1) amortized
Insert (middle)           O(n)
Delete (middle)           O(n)
Membership test           O(n)
Sort                      O(n log n)
Slice                     O(k)

Where k = size of slice

---

## 1.21 PERFORMANCE EXPERIMENT – APPEND VS INSERT

```python
import time

l = []
start = time.time()
for i in range(1000000):
    l.append(i)
print("Append time:", time.time() - start)

l = []
start = time.time()
for i in range(100000):
    l.insert(0, i)
print("Insert time:", time.time() - start)
```

Insert at beginning is significantly slower.

---

## 1.22 COPYING COMPLEX NESTED STRUCTURES – REAL BUG EXAMPLE

```python
original = [[1,2], [3,4]]
shallow = original.copy()

shallow[0][0] = 99
print(original)
```

Output:
[[99,2],[3,4]]

Because inner lists shared.

Correct deep copy:

```python
import copy

deep = copy.deepcopy(original)
deep[0][0] = 100
print(original)
```

---

## 1.23 LIST COMPREHENSION VS LOOP – MEMORY DIFFERENCE

```python
squares = [x*x for x in range(1000000)]
```

This creates entire list in memory.

Better alternative for large data:

```python
generator = (x*x for x in range(1000000))
```

Generator does not store full list.

---

## 1.24 WHEN NOT TO USE LIST

Do NOT use list when:

1. Frequent membership checking required → use set
2. Keys with values required → use dictionary
3. Data should not change → use tuple

---

## 1.25 ADVANCED EDGE CASE – MODIFYING WHILE ITERATING

Wrong:

```python
l = [1,2,3,4]
for x in l:
    if x % 2 == 0:
        l.remove(x)

print(l)
```

This can skip elements.

Correct way:

```python
l = [1,2,3,4]
l = [x for x in l if x % 2 != 0]
```

Or iterate over copy:

```python
for x in l[:]:
    if x % 2 == 0:
        l.remove(x)
```

---
## TUPLES

## 1. WHAT EXACTLY IS A TUPLE?

A tuple is:

* Ordered
* Immutable
* Allows duplicate elements
* Can store heterogeneous data types
* Stores references to objects (not raw values)

Basic example:

```python
t = (1, 2, 3)
print(type(t))
```

Important:
It is the comma that creates a tuple, not the parentheses.

```python
t = 1, 2, 3
print(type(t))
```

Single element tuple:

```python
t = (5,)      # Correct
x = (5)       # Just an int
print(type(t))
print(type(x))
```

## 2. INTERNAL REPRESENTATION

Like lists, tuples store references to objects.
But unlike lists, tuples do NOT support resizing.

This makes them:

* Memory efficient
* Slightly faster to iterate
* Safe from accidental modification

Check reference storage:

```python
x = 10
t = (x,)

print(id(x))
print(id(t[0]))
```

Both IDs will match.

## 3. IMMUTABILITY – COMPLETE UNDERSTANDING

Immutability means:

* Cannot change element
* Cannot append
* Cannot remove
* Cannot reassign index

Example:

```python
t = (1, 2, 3)
t[0] = 99
```

Raises:
TypeError

Why?
Because tuple memory layout is fixed at creation time.

## 4. SHALLOW IMMUTABILITY (VERY IMPORTANT)

Tuple immutability is shallow.

```python
t = ([1, 2], 3)

t[0].append(100)
print(t)
```

Output:
([1, 2, 100], 3)

Explanation:

* Tuple reference cannot change
* But referenced object (list) can change

Important conclusion:
Immutability applies to structure, not recursively to contents.

## 5. HASHABILITY – WHY TUPLES CAN BE DICTIONARY KEYS

Dictionary keys must be hashable.

Tuple is hashable only if all its elements are hashable.

Valid:

```python
d = {(1, 2): "valid"}
print(d[(1,2)])
```

Invalid:

```python
d = {([1,2], 3): "invalid"}
```

Raises:
TypeError: unhashable type: 'list'

Because list is mutable → not hashable.

Deep check:

```python
print(hash((1,2,3)))      # Works
print(hash((1,[2,3])))    # Error
```

## 6. MEMORY COMPARISON WITH LIST

```python
import sys

l = [1,2,3]
t = (1,2,3)

print(sys.getsizeof(l))
print(sys.getsizeof(t))
```

Tuple usually consumes less memory.

Reason:

* No overallocation strategy
* Fixed length

## 7. TUPLE UNPACKING – ALL CASES

### Basic unpacking:

```python
t = (10, 20, 30)
a, b, c = t
print(a, b, c)
```

### Mismatch case:

```python
a, b = (1,2,3)
```

Raises:
ValueError

### Extended unpacking:

```python
t = (1,2,3,4,5)
a, *b = t
print(a)
print(b)
```

### Unpacking in middle:

```python
a, *b, c = (1,2,3,4,5)
print(a)
print(b)
print(c)
```

Starred variable always becomes a list.

## 8. TUPLE CONCATENATION AND REPETITION

```python
t1 = (1,2)
t2 = (3,4)

print(t1 + t2)
print(t1 * 3)
```

### Important:
These operations create NEW tuples.
Original tuples remain unchanged.

## 9. TUPLE METHODS (LIMITED BY DESIGN)

Tuples have only two methods:

```python
t = (1,2,2,3)

print(t.count(2))
print(t.index(3))
```

### Why limited methods?
Because immutability removes need for modification methods.

## 10. IDENTITY vs EQUALITY WITH TUPLES

```python
a = (1,2,3)
b = (1,2,3)

print(a == b)   # True
print(a is b)   # Usually False
```

Do not rely on tuple interning.

## 11. USING TUPLES FOR STRUCTURED DATA

Tuples are good for fixed records.

```python
person = ("Jagriti", 21, "CSE")

name, age, branch = person
```

Better readability can be achieved with namedtuple (covered later).

## 12. TUPLE AS RETURN TYPE – BEST PRACTICE

```python
def divide(a, b):
    return a//b, a%b

q, r = divide(10, 3)
```

### Why tuple?
Because result structure should not change.

## 13. NESTED TUPLES – COMPLEX STRUCTURES

```python
t = ((1,2), (3,4))
print(t[0][1])
```

Fully immutable only if inner elements immutable.

## 14. PERFORMANCE MICRO TEST

```python
import time

start = time.time()
for _ in range(1000000):
    x = (1,2,3)
print("Tuple creation:", time.time() - start)

start = time.time()
for _ in range(1000000):
    x = [1,2,3]
print("List creation:", time.time() - start)
```

Tuple creation slightly faster in general.

## 15. WHEN NOT TO USE TUPLES

Do NOT use tuple when:

* Data needs modification
* Frequent updates required
* Order may change

### Use list instead.

## 16. ADVANCED EDGE CASE – MUTABLE ELEMENT SIDE EFFECT

```python
def modify(data):
    data[0].append(999)

original = ([1,2], 3)
modify(original)
print(original)
```

Even though tuple is immutable, side effects can occur via mutable elements.

## Important lesson:
Immutability does NOT guarantee deep safety.


