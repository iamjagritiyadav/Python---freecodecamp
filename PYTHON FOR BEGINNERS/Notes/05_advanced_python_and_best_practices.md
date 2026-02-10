# Advanced Python and Best Practices

## 1. Modules in Python

A module is a **file containing Python code** (functions, variables, classes).

```python
import math
print(math.sqrt(16))
```

### Types of Modules

* Built-in modules (`math`, `sys`, `os`)
* User-defined modules
* Third-party modules

### Why Modules Matter (Interview Why)

* Code reusability
* Separation of concerns
* Cleaner architecture

---

## 2. Command Line Arguments

Used to pass arguments while running the script.

```python
import sys
print(sys.argv)
```

```bash
python app.py 10 20
```

**Interview Use-case:**

* Automation scripts
* DevOps tools

---

## 3. Lambda Functions (Deep Perspective)

Anonymous, inline functions.

```python
lambda x: x * 2
```

### When to Use

* Short-lived logic
* Functional pipelines

### When NOT to Use

* Complex logic
* Multiple conditions

---

## 4. Decorators (VERY IMPORTANT)

Decorators modify behavior of functions **without changing their source code**.

### Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
```

```python
@my_decorator
def hello():
    print("Hello")
```

### Why Decorators Exist

* Logging
* Authentication
* Timing
* Caching

**Interview Reality:**

> Decorators = closures + functions

---

## 5. Docstrings

Docstrings describe **what a function/class does**.

```python
def add(a, b):
    """Returns sum of two numbers"""
    return a + b
```

### Why Interviewers Care

* Code readability
* Auto documentation

---

## 6. Type Annotations

Used to indicate expected data types.

```python
def add(a: int, b: int) -> int:
    return a + b
```

### Important Note

* Python does NOT enforce types
* Used by linters and IDEs

---

## 7. Exceptions and Error Handling

Exceptions prevent program crash and allow graceful handling.

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid input")
finally:
    print("Done")
```

### Custom Exceptions

```python
class MyError(Exception):
    pass
```

**Interview Trap:**

> Never use bare `except:`

---

## 8. The `with` Statement (Context Managers)

Used for **resource management**.

```python
with open("file.txt") as f:
    data = f.read()
```

### Why `with` Matters

* Auto cleanup
* Prevents memory leaks

---

## 9. Installing Packages with pip

```bash
pip install numpy
```

### Best Practices

* Use virtual environments
* Freeze dependencies

```bash
pip freeze > requirements.txt
```

---

## 10. List Comprehension (Advanced)

```python
[x*x for x in range(10) if x % 2 == 0]
```

### Performance Note

* Faster than loops
* But readability > cleverness

---

## 11. Polymorphism

Same interface, different behavior.

```python
class Bird:
    def fly(self):
        pass
```

```python
class Sparrow(Bird):
    def fly(self):
        print("Flying")
```

---

## 12. Operator Overloading

Customize operator behavior.

```python
class Point:
    def __add__(self, other):
        return Point(self.x + other.x)
```

### Common Magic Methods

* `__add__`
* `__str__`
* `__eq__`

---

## 13. Python Best Practices (INTERVIEW GOLD)

✅ Follow PEP8

✅ Use meaningful variable names

✅ Avoid global variables

✅ Write small functions

✅ Prefer readability over cleverness

---

## 14. Common Interview Traps

❌ Overusing decorators

❌ Catching all exceptions blindly

❌ Ignoring context managers

❌ No docstrings in functions

---

## 15. Rapid-Fire Interview Questions

1. What are decorators internally?
2. Why `with` is better than open/close?
3. Difference between annotation and type casting?
4. Why Python is not truly typed?
5. How pip resolves dependencies?

---

## 16. Answers

### 1. Decorators

They are functions that wrap other functions using closures.

### 2. `with`

Ensures automatic cleanup even if exception occurs.

### 3. Annotation vs Casting

Annotations suggest types; casting converts types.

### 4. Typing

Python is dynamically but strongly typed.

### 5. pip

Downloads and manages external packages.

