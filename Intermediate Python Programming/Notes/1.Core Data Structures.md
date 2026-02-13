# Core Data Structures 

# Lists

## What is a List?

A list is an ordered, mutable, dynamic array structure in Python.

* Ordered → maintains insertion order
* Mutable → can be modified after creation
* Allows duplicate values
* Heterogeneous → can store different data types

## Memory Behavior

Lists store references to objects, not the actual objects themselves. Internally implemented as dynamic arrays.

When capacity is exceeded, Python allocates a larger block and copies references.

## Creation

```python
numbers = [1, 2, 3]
empty = []
constructed = list((4, 5, 6))
```

## Indexing

```python
numbers[0]      # First element
numbers[-1]     # Last element
```

Time Complexity → O(1)

## Slicing

```python
numbers[0:2]
numbers[::-1]   # Reverse
```

Slicing creates a new list (shallow copy of references).

## Modifying Lists

```python
numbers.append(4)
numbers.insert(1, 10)
numbers.remove(2)
del numbers[0]
numbers.pop()
```

## List Comprehension

```python
squares = [x*x for x in range(10)]
```

More efficient and readable than loops.

## Copying

Shallow Copy:

```python
copy1 = numbers.copy()
copy2 = numbers[:]
```

Deep Copy:

```python
import copy
copy.deepcopy(numbers)
```

---

# Tuples

## What is a Tuple?

An ordered, immutable collection.

```python
t = (1, 2, 3)
```

## Immutability

Elements cannot be changed after creation.

## Why Use Tuples?

* Faster than lists
* Safe from modification
* Can be dictionary keys

## Tuple Unpacking

```python
a, b, c = (1, 2, 3)
```

## Single Element Tuple

```python
x = (5,)
```

---

# Dictionaries

## What is a Dictionary?

Unordered (Python 3.7+ ordered by insertion), mutable key-value mapping.

```python
person = {"name": "Jagriti", "age": 20}
```

## Internal Working

Implemented using hash tables.

Average Time Complexity → O(1)

## Accessing Values

```python
person["name"]
person.get("age")
```

Use `.get()` to avoid KeyError.

## Iteration

```python
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)
```

## Copying

```python
copy_dict = person.copy()
```

## Dictionary Comprehension

```python
squares = {x: x*x for x in range(5)}
```

---

# Sets

## What is a Set?

Unordered collection of unique elements.

```python
s = {1, 2, 3}
```

Duplicates automatically removed.

## Set Operations

Union

```python
a | b
```

Intersection

```python
a & b
```

Difference

```python
a - b
```

Symmetric Difference

```python
a ^ b
```

## Use Case

Fast membership testing.

Time Complexity → O(1) average

---

# Strings

## What is a String?

Immutable sequence of characters.

```python
text = "hello"
```

## String Slicing

```python
text[0:2]
text[::-1]
```

## Common Methods

```python
text.upper()
text.lower()
text.split()
" ".join(["hello", "world"])
```

## String Formatting

```python
name = "Jagriti"
print(f"Hello {name}")
```

## Performance Tip

Use `join()` instead of + in loops for concatenation.

---

# Summary

Lists → Flexible dynamic arrays
Tuples → Immutable optimized sequences
Dictionaries → Fast key-value lookup
Sets → Unique elements, fast membership
Strings → Immutable text handling

