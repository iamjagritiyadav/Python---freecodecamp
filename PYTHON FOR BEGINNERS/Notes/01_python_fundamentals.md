# Python Fundamentals

## 1. Introduction to Python

Python is a **high-level, interpreted, dynamically typed, and general-purpose programming language**. It focuses on readability and simplicity while being powerful enough for large-scale systems.

### Key Features

* Simple and readable syntax
* Interpreted (no separate compilation step)
* Dynamically typed (type decided at runtime)
* Large standard library
* Cross-platform
* Supports multiple paradigms: procedural, OOP, functional

### Where Python is Used

* Web Development (Django, Flask)
* Data Science & ML
* Automation & Scripting
* DevOps
* Backend Systems

**Interview Tip:**

> Python trades execution speed for developer productivity.

---

## 2. Variables & Naming Rules

Variables are **labels that reference objects in memory**, not fixed memory containers.

```python
x = 10
name = "Jagriti"
```

### Naming Rules

* Must start with a letter or `_`
* Cannot start with a number
* Case-sensitive (`age` ≠ `Age`)
* Cannot be a reserved keyword

Valid:

```python
_age = 21
user_name = "abc"
```

Invalid:

```python
2name = "x"  # SyntaxError
class = 10    # Keyword
```

**Interview Tip:**

> Python variables point to objects, they don’t store values directly.

---

## 3. Expressions & Statements

### Expression

Anything that **returns a value**.

```python
x + 5
len("python")
```

### Statement

An instruction that performs an action.

```python
x = 10
print(x)
```

**Key Difference (Interview Favorite):**

* Expressions produce values
* Statements perform actions

---

## 4. Comments

Used to explain code and improve readability.

### Single-line Comment

```python
# This is a comment
```

### Multi-line Comment (Convention)

```python
"""
This is a multi-line comment
"""
```

**Best Practice:**

* Explain *why*, not *what*

---

## 5. Data Types (Overview)

Python is dynamically typed, but strongly typed.

### Built-in Data Types

* `int`
* `float`
* `complex`
* `bool`
* `str`
* `list`
* `tuple`
* `set`
* `dict`
* `NoneType`

```python
type(10)        # int
type("hi")      # str
type(True)      # bool
```

**Interview Tip:**

> Dynamic typing ≠ weak typing.

---

## 6. Numbers & Booleans

### Number Types

```python
a = 10        # int
b = 3.14      # float
c = 2 + 3j    # complex
```

### Boolean Values

```python
True
False
```

Used heavily in conditions:

```python
if 5 > 3:
    print("Correct")
```

**Truthiness (Important):**

* `0`, `None`, `""`, `[]` → False
* Everything else → True

---

## 7. Strings

Strings are **immutable sequences of characters**.

```python
s = "Python"
```

### Common Operations

```python
s.upper()
s.lower()
s.replace("P", "J")
```

---

## 8. String Methods

Frequently used string methods:

```python
text = "hello world"

text.upper()
text.lower()
text.title()
text.strip()
text.split()
text.find("world")
```

**Interview Tip:**

> Strings are immutable — methods return new strings.

---

## 9. Escaping Characters

Used to insert special characters inside strings.

```python
print("Hello\nWorld")
print("He said, \"Python is easy\"")
```

Common escape characters:

* `\n` → New line
* `\t` → Tab
* `\\` → Backslash

---

## 10. Indexing & Slicing

### Indexing

```python
s = "Python"
s[0]   # 'P'
s[-1]  # 'n'
```

### Slicing

```python
s[0:3]   # 'Pyt'
s[:4]    # 'Pyth'
s[::2]   # 'Pto'
```

**Interview Trap:**

> Strings cannot be modified in-place.

---

## 11. Built-in Functions

Common built-ins:

```python
len()
type()
range()
print()
input()
int()
float()
str()
```

Example:

```python
x = input("Enter number: ")
x = int(x)
```

---

## 12. User Input

```python
name = input("Enter your name: ")
print(name)
```

**Important:**

* Input is always string by default

---

## 13. Enums

Enums are used to define a set of **named constants**.

```python
from enum import Enum

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 0
```

Usage:

```python
print(Status.ACTIVE)
```

**Interview Use-case:**

* Avoid magic numbers
* Improve code readability

---

## 14. Common Mistakes (Interview Section)

❌ Assuming input() returns int

```python
age = input()
```

✅ Correct:

```python
age = int(input())
```

❌ Modifying strings directly

❌ Confusing `=` with `==`

❌ Poor variable naming

---

## 15. Quick Interview Questions

* Why is Python called dynamically typed?
* Difference between expression and statement?
* Why strings are immutable?
* What is truthy and falsy?
* Difference between `is` and `==`?

---

## Final Notes

Mastering these fundamentals makes **every advanced topic easier**. If this file is strong, your entire Python foundation is strong.

Next: `02_operators_and_control_flow.md`
