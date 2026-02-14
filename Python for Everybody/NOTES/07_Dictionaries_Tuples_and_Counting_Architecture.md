
# Dictionaries, Tuples & Counting Architecture 

This section explains how dictionaries and tuples work internally and how they are used to design efficient counting and aggregation systems.

Dictionaries are one of the most powerful data structures in Python. Understanding their internal mechanics is critical for writing scalable programs.

---

# 1. Dictionary – Internal Architecture

A dictionary in Python is implemented using a **hash table**.

Core idea:

* Keys are hashed
* Hash value determines storage location
* Lookup is O(1) average time

Example:

```python
d = {"a": 1, "b": 2}
```

Internally:

1. Python computes `hash("a")`
2. Maps it to an index in internal array
3. Stores key-value pair at that location

Dictionary stores:

* Hash of key
* Key object reference
* Value object reference

---

# 2. Why Keys Must Be Immutable

Dictionary keys must be:

* Hashable
* Immutable

Examples of valid keys:

* int
* float
* str
* tuple (if elements immutable)

Invalid key example:

```python
d = {[1,2]: "value"}  # Error
```

Why?

If key changes after insertion, hash changes → dictionary cannot find it.

---

# 3. Hash Collisions

Two different keys can produce same hash.

Python handles collisions using:

* Open addressing
* Probing strategy

Even with collisions, lookup remains efficient in most cases.

Worst case complexity: O(n)
Average case: O(1)

---

# 4. Dictionary Operations Complexity

| Operation | Average Time |
| --------- | ------------ |
| Lookup    | O(1)         |
| Insert    | O(1)         |
| Delete    | O(1)         |
| Iteration | O(n)         |

Understanding this helps in performance decisions.

---

# 5. Counting Pattern (Core Architecture)

Classic word frequency example:

```python
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
```

This is a fundamental counting architecture.

Execution logic:

1. Iterate words
2. Check membership (hash lookup)
3. Update count

Efficient due to constant-time lookup.

---

# 6. Simplified Counting with get()

```python
counts[word] = counts.get(word, 0) + 1
```

Mechanism:

* If key exists → return value
* Else → return default 0
* Add 1
* Store result

Reduces branching.

---

# 7. Dictionary as Data Model

Dictionaries are ideal for:

* Mapping relationships
* Fast lookup tables
* Caching
* Configuration storage

Example data modeling:

```python
student = {
    "name": "Jagriti",
    "age": 20,
    "skills": ["Python", "ML"]
}
```

Flexible but must be used thoughtfully.

---

# 8. Iterating Over Dictionary

```python
for key in d:
for key, value in d.items():
```

Internally:

Dictionary iterator walks through internal table skipping empty slots.

---

# 9. Sorting a Dictionary

Dictionaries themselves are insertion-ordered (Python 3.7+),
but not sorted.

To sort by key:

```python
sorted(d.items())
```

To sort by value:

```python
sorted(d.items(), key=lambda x: x[1])
```

Sorting complexity = O(n log n)

---

# 10. Tuples – Why They Matter

Tuples are:

* Ordered
* Immutable
* Hashable (if contents immutable)

Example:

```python
t = (1, 2, 3)
```

Why use tuples?

* Lightweight
* Safe from modification
* Can act as dictionary keys

---

# 11. Tuple Unpacking

```python
for key, value in d.items():
    print(key, value)
```

Each iteration returns tuple `(key, value)`.

Python automatically unpacks.

---

# 12. Sorting Dictionary Using Tuples

Common pattern:

```python
pairs = []
for key, value in d.items():
    pairs.append((value, key))

pairs.sort(reverse=True)
```

Why reverse order of elements?

Because tuple comparison is lexicographic.
It compares first element first.

This allows sorting by value.

---

# 13. Lexicographic Ordering in Tuples

Tuple comparison rule:

Compare element by element.

Example:

```python
(2, "a") > (1, "z")   # True
```

Because 2 > 1.

Used heavily in ranking systems.

---

# 14. Memory Considerations

Dictionary:

* Higher memory overhead
* Fast lookup

List:

* Lower overhead
* Slower membership testing (O(n))

Choose based on problem.

---

# 15. Real-World Data Aggregation Pattern

Pipeline:

1. Read data
2. Extract key
3. Update dictionary count
4. Convert to list of tuples
5. Sort
6. Display top results

This architecture is used in:

* Log analysis
* Word frequency
* Analytics dashboards
* Ranking systems

---

# 16. Common Mistakes

* Using mutable object as dictionary key
* Forgetting default value in counting
* Sorting dictionary repeatedly inside loop
* Confusing key vs value iteration

---

# Summary

* Dictionaries use hash tables for O(1) lookup.
* Keys must be immutable and hashable.
* Counting architecture is fundamental in analytics.
* Tuples enable efficient sorting strategies.
* Combined dictionary + tuple pattern forms ranking systems.

Mastering dictionaries means mastering fast data lookup and aggregation.
