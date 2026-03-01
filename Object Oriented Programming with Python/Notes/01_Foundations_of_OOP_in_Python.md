# 01 – Foundations of OOP in Python

## 1. Why Object Oriented Programming?

Object Oriented Programming (OOP) is a programming paradigm that structures code around **objects** rather than just functions and logic blocks.

In real-world software systems:

* Data and behavior belong together.
* Systems grow in size and complexity.
* Code must be reusable and maintainable.

Without OOP, managing large-scale systems becomes chaotic due to scattered variables and repeated logic.

The core idea:

> Group related data and functionality together inside a blueprint called a **class**.

---

## 2. Everything in Python is an Object

One of the most important conceptual foundations:

In Python:

* Strings are objects
* Integers are objects
* Lists are objects
* Functions are objects
* Classes are objects

Example:

```python
x = "hello"
print(type(x))
```

Output:

```
<class 'str'>
```

This means:

* `"hello"` is not primitive data.
* It is an **instance of class `str`**.

Similarly:

```python
print(type(10))
```

Output:

```
<class 'int'>
```

So when we create our own classes, we are simply creating **new data types**.

---

## 3. The Problem Without OOP

Imagine building a store management system.

Without OOP:

```python
item1_name = "Phone"
item1_price = 100
item1_quantity = 5

item2_name = "Laptop"
item2_price = 1000
item2_quantity = 3
```

Problems:

* No real relationship between these variables.
* Naming conventions are doing fake grouping.
* Hard to scale to 100 items.
* Code duplication.

Python sees these as completely separate variables.

There is no structure.

---

## 4. Introducing Classes

A class is a blueprint for creating objects.

Basic structure:

```python
class Item:
    pass
```

Creating an object (instance):

```python
item1 = Item()
item2 = Item()
```

This is equivalent to how Python creates built-in types:

```python
s = str("hello")
```

Instantiation means:

> Creating an object from a class.

---

## 5. Attributes (Data Inside Objects)

We can assign attributes dynamically:

```python
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
```

Now these values are tied to a specific object.

Difference from random variables:

* Attributes belong to an object.
* They are accessed using dot notation.
* They create structured grouping.

Checking type:

```python
print(type(item1))
```

Output:

```
<class '__main__.Item'>
```

We created a custom data type.

---

## 6. Instance vs Class Conceptual Model

When you write:

```python
item1 = Item()
```

Internally:

* Memory is allocated.
* An object is created.
* A reference is stored in `item1`.

You can verify object attributes using:

```python
print(item1.__dict__)
```

This shows all instance-level attributes.

---

## 7. Methods (Behavior Inside Classes)

Methods are functions defined inside a class.

Example:

```python
class Item:
    def calculate_total_price(self, x, y):
        return x * y
```

Calling method:

```python
item1.calculate_total_price(100, 5)
```

Important Concept:
When calling:

```python
item1.calculate_total_price(100, 5)
```

Python internally converts it to:

```python
Item.calculate_total_price(item1, 100, 5)
```

That is why `self` is mandatory.

`self` refers to the instance itself.

---

## 8. Why `self` is Required

If you remove `self`:

```python
def calculate_total_price():
    pass
```

You get:

```
TypeError: takes 0 positional arguments but 1 was given
```

Because Python automatically passes the instance as the first argument.

Convention:

* Always name it `self`.

---

## 9. Improving the Design (Constructor Introduction)

Problem:
Manually assigning attributes after instantiation is bad practice.

Solution: Constructor (`__init__`)

```python
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
```

Now:

```python
item1 = Item("Phone", 100, 5)
```

Advantages:

* Enforces required parameters.
* Prevents incomplete objects.
* Cleaner and scalable.

---

## 10. Default Parameters in Constructors

```python
def __init__(self, name, price, quantity=0):
```

If quantity is unknown:

```python
item1 = Item("Phone", 100)
```

Default value is used.

---

## 11. Type Hints (Improving Reliability)

```python
def __init__(self, name: str, price: float, quantity: int = 0):
```

Benefits:

* Better readability
* IDE validation
* Fewer bugs

Note:
Type hints do not enforce at runtime.
They are annotations.

---

## 12. Input Validation with `assert`

We must prevent invalid values.

```python
assert price >= 0, f"Price {price} must be >= 0"
assert quantity >= 0, f"Quantity {quantity} must be >= 0"
```

Why this matters:

* Defensive programming
* Early failure
* Clean data integrity

---

## 13. Clean OOP Mental Model

An object consists of:

1. State → Attributes
2. Behavior → Methods

A class defines:

* What attributes exist
* What actions can be performed

---

## 14. Attribute Lookup Flow

When accessing:

```python
item1.price
```

Python checks:

1. Instance dictionary (`item1.__dict__`)
2. Class dictionary (`Item.__dict__`)
3. Parent classes (if any)

This lookup mechanism is foundational for understanding inheritance later.

---

## 15. Key Takeaways

* Python is fully object-oriented.
* Classes create custom data types.
* Objects store state and behavior together.
* `self` represents the current instance.
* Constructors initialize object state.
* Type hints improve clarity.
* `assert` enforces constraints.
* Attribute lookup follows instance → class hierarchy.

This foundation is critical before moving to advanced topics like class attributes, inheritance, magic methods, and encapsulation.

