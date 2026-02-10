# Functions and Object-Oriented Programming

## 1. Functions in Python

A function is a **reusable block of code** that performs a specific task.

```python
def add(a, b):
    return a + b
```

### Why Functions Exist (Interview Why)

* Code reusability
* Modularity
* Maintainability
* Testability

---

## 2. Function Arguments (Deep Dive)

### Positional Arguments

```python
add(2, 3)
```

### Keyword Arguments

```python
add(a=2, b=3)
```

### Default Arguments (VERY IMPORTANT)

```python
def power(x, y=2):
    return x ** y
```

❌ **Mutable Default Argument Trap**

```python
def f(x, arr=[]):
    arr.append(x)
    return arr
```

**Why dangerous?**

* Default arguments evaluated once
* Same list reused across calls

✅ Correct way:

```python
def f(x, arr=None):
    if arr is None:
        arr = []
    arr.append(x)
    return arr
```

---

## 3. *args and **kwargs

Used for variable-length arguments.

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)
```

**Interview Use-case:**

* API design
* Decorators

---

## 4. Return Statement

* A function can return multiple values
* Returned as tuple

```python
def stats(x, y):
    return x+y, x*y
```

---

## 5. Variable Scope – LEGB Rule (INTERVIEW FAVORITE)

Python resolves variables in this order:

1. **Local**
2. **Enclosing**
3. **Global**
4. **Built-in**

```python
x = 10

def outer():
    x = 20
    def inner():
        print(x)
    inner()
```

Output: `20`

---

### global vs nonlocal

```python
x = 10

def f():
    global x
    x = 20
```

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
```

---

## 6. Nested Functions

Functions inside functions.

```python
def outer():
    def inner():
        return "hello"
    return inner
```

---

## 7. Closures (EXTREMELY IMPORTANT)

A closure is a function that **remembers variables from its enclosing scope** even after that scope has finished execution.

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(3))  # 8
```

**Why Interviewers Love Closures**

* Tests understanding of scope
* Used in decorators

---

## 8. Lambda Functions

Anonymous one-line functions.

```python
square = lambda x: x*x
```

**Limitations:**

* Single expression only
* No statements

---

## 9. Map, Filter, Reduce

### map

```python
list(map(lambda x: x*2, [1,2,3]))
```

### filter

```python
list(filter(lambda x: x%2==0, [1,2,3,4]))
```

### reduce

```python
from functools import reduce
reduce(lambda a,b: a+b, [1,2,3])
```

**Interview Note:**

> Prefer list comprehension for readability.

---

## 10. Recursion

Function calling itself.

```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
```

### Recursion Stack

* Each call adds a stack frame
* Risk: stack overflow

---

## 11. Object-Oriented Programming (OOP)

OOP is about **modeling real-world entities**.

Core Pillars:

* Encapsulation
* Abstraction
* Inheritance
* Polymorphism

---

## 12. Classes and Objects

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi {self.name}"
```

---

## 13. **init** Method

* Constructor
* Automatically called

```python
p = Person("A")
```

---

## 14. Instance vs Class Variables

```python
class A:
    x = 10
    def __init__(self):
        self.y = 20
```

---

## 15. Inheritance

```python
class A:
    def show(self):
        print("A")

class B(A):
    pass
```

---

## 16. Polymorphism

Same method name, different behavior.

```python
class Dog:
    def speak(self):
        print("Bark")
```

---

## 17. Method Overriding

```python
class B(A):
    def show(self):
        print("B")
```

---

## 18. Operator Overloading

```python
class Point:
    def __add__(self, other):
        return Point(self.x + other.x)
```

---

## 19. Interview Traps

❌ Confusing class vs instance variables

❌ Misusing global variables

❌ Not understanding closures

---

## 20. Rapid-Fire Interview Questions

1. What is LEGB rule?
2. Why closures exist?
3. Difference between class and object?
4. Why Python supports multiple inheritance?
5. When NOT to use recursion?

---

## 21. Answers

### 1. LEGB Rule

Order Python follows to resolve variables.

### 2. Closures

They preserve state without global variables.

### 3. Class vs Object

Class is blueprint, object is instance.

### 4. Multiple Inheritance

Allows reuse but increases complexity.

### 5. Recursion Limit

Risk of stack overflow.

---
