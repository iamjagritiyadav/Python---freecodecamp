# Advanced Concepts

# Decorators

## What is a Decorator?

A decorator is a function that modifies or extends the behavior of another function without changing its actual source code.

Functions in Python are first-class objects. This means:

* They can be assigned to variables
* Passed as arguments
* Returned from other functions

Decorator syntax:

```python
@decorator_name
def function():
    pass
```

This is equivalent to:

```python
function = decorator_name(function)
```

---

## Basic Decorator Example

```python
def my_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
```

Execution flow:

1. say_hello is passed into my_decorator
2. wrapper replaces original function
3. wrapper executes additional logic

---

## Decorator with Arguments

Problem: What if original function takes parameters?

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper
```

Using *args and **kwargs makes decorator generic.

---

## Preserving Metadata (wraps)

Without wraps, original function name and docstring are lost.

```python
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

wraps preserves:

* **name**
* **doc**
* **module**

Important in large systems and frameworks.

---

## Decorator with Its Own Arguments

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi")
```

Here execution flow becomes:
repeat(3) → decorator → wrapper

---

# Generators

## What is a Generator?

A generator is a function that returns an iterator using the yield keyword.

Unlike normal functions:

* Does not execute fully at once
* Pauses state
* Resumes from last yield

---

## Example

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```

Each call to next() resumes execution.

---

## Why Generators?

Memory Efficient:

* Does not store full list
* Generates values on demand

Compare:

```python
[x for x in range(10**7)]   # Large memory
(x for x in range(10**7))   # Generator expression
```

---

## Generator Expression

```python
gen = (x*x for x in range(5))
```

Lazy evaluation.

---

## Generator Internals

When function contains yield:

* Python creates generator object
* Execution suspended at yield
* Local variables preserved in frame

Generator states:

* Created
* Running
* Suspended
* Exhausted

---

# Shallow vs Deep Copy

Understanding memory references is critical.

---

## Shallow Copy

Copies outer container only.
Nested objects remain shared.

```python
import copy

original = [[1,2],[3,4]]
shallow = copy.copy(original)
```

Changing nested list affects both.

---

## Deep Copy

Recursively copies everything.

```python
deep = copy.deepcopy(original)
```

Now modifications are independent.

---

## Why It Matters

Common bug in:

* Machine learning pipelines
* Nested config dictionaries
* State management systems

---

# Context Managers

## What is a Context Manager?

A construct that properly manages resources.

Used with `with` statement.

Example:

```python
with open("file.txt") as f:
    data = f.read()
```

Automatically closes file.

---

## How It Works Internally

Context manager must implement:

* **enter**()
* **exit**()

Example:

```python
class MyContext:
    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit")
```

**exit** handles exceptions.

---

## Using contextlib

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Start")
    yield
    print("End")
```

Cleaner way to write context managers.

---

# Summary

Decorators → Modify behavior dynamically
Generators → Memory-efficient lazy execution
Shallow vs Deep Copy → Understand object references
Context Managers → Safe resource handling

These concepts are heavily used in frameworks like Django, FastAPI, TensorFlow, and production backend systems.
