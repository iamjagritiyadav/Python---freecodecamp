
# Strings: Internal Working & Parsing

Strings look simple.
But internally they involve encoding, immutability rules, memory allocation strategies, and performance trade-offs.

This document explains:

* How Python stores strings
* Why strings are immutable
* Encoding (ASCII vs UTF-8)
* str vs bytes
* Efficient string operations
* Real-world parsing strategies
* Performance traps

---

# 1. What Is a String Internally?

A Python string is:

* An immutable sequence of Unicode characters
* Stored as an object in heap memory
* Represented internally in optimized form (CPython uses flexible string representation)

Example:

```python
s = "hello"
```

Internally:

1. A string object is created.
2. Memory allocated to store characters.
3. Variable `s` references that object.

Important:
The string object contains metadata:

* Length
* Hash value (cached)
* Encoding strategy

---

# 2. Immutability – Why Strings Cannot Change

Example:

```python
s = "hello"
s[0] = 'H'   # Error
```

Why?

Strings are immutable.

Benefits of immutability:

1. Safer memory sharing
2. Cached hash values (important for dictionary keys)
3. Thread safety
4. Optimization by interpreter

When you "modify" a string:

```python
s = s + " world"
```

Python creates a new string object.
Old string remains unchanged.
Variable now points to new object.

---

# 3. String Interning

Python sometimes reuses identical string literals.

Example:

```python
a = "hello"
b = "hello"
```

Often `a` and `b` point to same object.

This optimization is called interning.

Used for:

* Small strings
* Identifiers

Improves memory efficiency.

---

# 4. Encoding – ASCII vs Unicode vs UTF-8

Computers store data as bytes.

Characters must be encoded into bytes.

## ASCII

* 7-bit encoding
* 128 characters
* Limited to English letters and symbols

## Unicode

* Universal character set
* Supports global languages

## UTF-8

* Variable-length encoding for Unicode
* 1–4 bytes per character
* Backward compatible with ASCII

Python 3 uses Unicode for `str`.

---

# 5. str vs bytes

In Python:

* `str` → sequence of Unicode characters
* `bytes` → sequence of raw 8-bit values

Example:

```python
text = "hello"
data = b"hello"
```

Key difference:

`str` represents text.
`bytes` represents raw binary data.

---

# 6. Encoding & Decoding

When working with network or files:

```python
text = "hello"
encoded = text.encode('utf-8')

raw = b"hello"
decoded = raw.decode('utf-8')
```

encode() → str → bytes
decode() → bytes → str

This is critical in:

* Socket programming
* File handling
* APIs

---

# 7. Indexing & Slicing Mechanics

Example:

```python
s = "abcdef"
s[2]      # 'c'
s[1:4]    # 'bcd'
```

Indexing:

* O(1) operation

Slicing:

* Creates new string
* Time complexity O(k)

Because string is immutable, slice must allocate new object.

---

# 8. String Concatenation Performance

Bad practice:

```python
result = ""
for word in words:
    result += word
```

Each iteration:

* Creates new string
* Copies old content

Time complexity becomes O(n²).

Better:

```python
"".join(words)
```

join():

* Calculates final size
* Allocates once
* Efficient O(n)

---

# 9. Common String Methods (Internal Perspective)

## split()

```python
s.split(',')
```

Creates list of substrings.
Allocates new string objects.

---

## strip()

Removes leading/trailing whitespace.
Returns new string.

---

## replace()

Creates new string with replacements.
Does NOT modify original.

---

## find() vs index()

* find() → returns -1 if not found
* index() → raises ValueError

Use find() for safer search.

---

# 10. Parsing Strategies (Real Engineering Thinking)

Parsing means extracting structured data from text.

Three main strategies:

---

## 10.1 Using split()

Best when delimiter is consistent.

Example:

```python
line = "name,age,city"
data = line.split(',')
```

Fast and simple.

---

## 10.2 Using slicing

Useful when structure fixed by position.

Example:

```python
date = "2025-07-17"
year = date[:4]
```

---

## 10.3 Using Regular Expressions

When structure is complex or inconsistent.

More powerful but slower.

---

# 11. Memory Behavior of Large Strings

If reading large file:

```python
content = file.read()
```

Loads entire file into memory.

Better:

```python
for line in file:
```

Lazy iteration.
Lower memory usage.

---

# 12. Unicode Pitfalls

Common issue:

Mixing str and bytes.

```python
"hello" + b"world"   # Error
```

Always decode bytes before combining with strings.

---

# 13. f-Strings and Formatting

Example:

```python
name = "Jagriti"
f"Hello {name}"
```

f-strings evaluated at runtime.
More readable and efficient than concatenation.

---

# 14. String Hashing

Strings are hashable.

This allows use as dictionary keys.

Hash value cached after first computation.
Improves performance in repeated lookups.

---

# 15. Common String Mistakes

* Using + in loop for large data
* Forgetting encoding/decoding in networking
* Confusing bytes and str
* Off-by-one slicing errors

---

# Summary

* Strings are immutable Unicode objects.
* Internally optimized with flexible storage.
* Modifications create new objects.
* join() is preferred for concatenation.
* Encoding/decoding critical in networking.
* Parsing strategy depends on structure complexity.

Deep understanding of strings is essential for file processing, APIs, regex, and networking.
