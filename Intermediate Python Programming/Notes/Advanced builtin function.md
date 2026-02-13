# Advanced Built-in Tools

# Collections Module

The collections module extends Python’s built-in container types with specialized data structures.

## Counter

Purpose: Count frequency of elements.

```python
from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
c = Counter(nums)
print(c)
```

Internal Concept:

* Subclass of dict
* Keys → elements
* Values → frequency

Useful Methods:

```python
c.most_common(1)
c.update([2,2])
c.subtract([3])
```

Time Complexity → O(n)

Use Case:

* Frequency problems
* Anagram checking
* Voting systems

---

## defaultdict

Purpose: Automatically assigns default value if key doesn’t exist.

```python
from collections import defaultdict

d = defaultdict(int)
d["a"] += 1
```

Without defaultdict → KeyError.
With defaultdict → auto-initialization.

Common Default Types:

* int → 0
* list → []
* set → set()

---

## deque

Double-ended queue.

```python
from collections import deque

d = deque([1,2,3])
d.appendleft(0)
d.pop()
```

Time Complexity:

* O(1) append/pop from both ends
* Faster than list for queue operations

Use Case:

* Sliding window problems
* BFS traversal

---

## namedtuple

Creates tuple-like objects with named fields.

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(1,2)
print(p.x)
```

Immutable but readable.

---

# Itertools Module

Provides memory-efficient iterator building blocks.

Works lazily → does not store full result in memory.

## product

```python
from itertools import product

list(product([1,2], [3,4]))
```

Cartesian product.

---

## permutations

```python
from itertools import permutations

list(permutations([1,2,3], 2))
```

Order matters.

---

## combinations

```python
from itertools import combinations

list(combinations([1,2,3], 2))
```

Order does not matter.

---

## accumulate

```python
from itertools import accumulate

list(accumulate([1,2,3,4]))
```

Produces cumulative sums.

---

## groupby

```python
from itertools import groupby

data = [1,1,2,2,2,3]
for key, group in groupby(data):
    print(key, list(group))
```

Important: Data must be sorted first.

---

# Lambda Functions

Anonymous one-line functions.

```python
square = lambda x: x*x
```

Limitations:

* Single expression only
* No statements

Used with:

* sort
* map
* filter

---

# Function Arguments

Understanding argument passing is critical.

## Positional Arguments

```python
def add(a, b):
    return a + b
```

## Keyword Arguments

```python
add(a=2, b=3)
```

## Default Arguments

```python
def greet(name="Guest"):
    print(name)
```

Important Trap:
Default mutable arguments persist across calls.

Bad Practice:

```python
def func(lst=[]):
    lst.append(1)
```

Correct Way:

```python
def func(lst=None):
    if lst is None:
        lst = []
```

---

# *args and **kwargs

## *args

Collects extra positional arguments into tuple.

```python
def func(*args):
    print(args)
```

## **kwargs

Collects extra keyword arguments into dictionary.

```python
def func(**kwargs):
    print(kwargs)
```

Order Rule:

```python
def func(positional, *args, default=1, **kwargs):
    pass
```

---

# Asterisk (*) Operator Usage

## Unpacking Lists

```python
nums = [1,2,3]
print(*nums)
```

## Merging Lists

```python
merged = [*a, *b]
```

## Merging Dictionaries

```python
merged = {**d1, **d2}
```

## Extended Unpacking

```python
a, *middle, b = [1,2,3,4,5]
```

---

# Summary

collections → Specialized containers
itertools → Memory-efficient iteration tools
lambda → Inline anonymous functions
Function arguments → Control flexibility and safety

* operator → Unpacking and merging power tool

These tools make your Python code concise, expressive, and production-ready.
