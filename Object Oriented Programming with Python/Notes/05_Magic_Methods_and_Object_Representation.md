# 05 – Magic Methods and Object Representation 

This section is extremely important for writing professional-grade Python classes.

Magic methods (also called **dunder methods**) allow you to control:

* How objects are created
* How objects are printed
* How objects behave with operators
* How objects behave in built-in functions
* How objects integrate with Python’s data model

Understanding this properly separates beginner OOP from advanced Python engineering.

---

# 1. What Are Magic Methods?

Magic methods are special methods that:

* Start and end with double underscores
* Are automatically triggered by Python
* Integrate your class with Python’s internal behavior

Examples:

```
__init__
__repr__
__str__
__len__
__add__
__eq__
__new__
__del__
```

They are not called directly (usually).
They are invoked implicitly.

---

# 2. Why Object Representation Matters

By default, when you print an object:

```python
print(item1)
```

You see something like:

```
<__main__.Item object at 0x000001F3A0B7E8E0>
```

This is useless for debugging.

It tells you:

* Memory address
* Class name

But nothing about the object’s state.

Professional classes always implement meaningful representations.

---

# 3. `__repr__` – The Developer Representation

Purpose:

Return a string representation of the object for debugging.

Example from store system:

```python
class Item:
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
```

Now:

```python
print(item1)
```

Output:

```
Item('Phone', 100, 5)
```

Much cleaner.

---

# 4. Official Philosophy of `__repr__`

Best practice (from Python docs):

`__repr__` should return a string that:

* Is unambiguous
* Ideally can recreate the object

Meaning:

```python
Item('Phone', 100, 5)
```

Should allow you to do:

```python
eval(repr(item1))
```

And recreate the object.

This is not mandatory, but ideal.

---

# 5. `__str__` vs `__repr__`

Two similar methods, different purposes.

## `__repr__`

* Developer-focused
* Detailed
* Unambiguous
* Used in debugging

## `__str__`

* User-friendly
* Clean display
* Simpler formatting

Example:

```python
class Item:
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name} – ${self.price}"
```

Behavior:

```python
print(item1)         # Uses __str__
item1                # Uses __repr__ in interactive shell
```

If `__str__` not defined → Python falls back to `__repr__`.

---

# 6. How Python Chooses Which to Use

When printing:

* `print(obj)` → calls `str(obj)` → uses `__str__`
* `repr(obj)` → uses `__repr__`
* Interactive shell → prefers `__repr__`

Internal flow:

```
str(obj) -> obj.__str__()
repr(obj) -> obj.__repr__()
```

---

# 7. Dynamic Class Name in `__repr__`

Hardcoding class name is bad practice.

Bad:

```python
return f"Item('{self.name}', {self.price})"
```

Better:

```python
return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
```

Why?

If subclass inherits representation, it prints correct class name automatically.

This becomes important in inheritance scenarios.

---

# 8. Using Magic Methods to Improve Debugging

Without `__repr__`:

```
[<Item object at 0x001>, <Item object at 0x002>]
```

With `__repr__`:

```
[Item('Phone', 100, 5), Item('Laptop', 1000, 3)]
```

Huge improvement.

Especially useful when printing lists of objects.

---

# 9. Other Important Magic Methods

## `__len__`

Controls behavior of `len()`.

```python
class Item:
    def __len__(self):
        return self.quantity
```

Now:

```python
len(item1)
```

Returns quantity.

---

## `__add__`

Controls `+` operator.

```python
class Item:
    def __add__(self, other):
        return self.quantity + other.quantity
```

Now:

```python
item1 + item2
```

Custom logic executed.

---

## `__eq__`

Controls equality comparison.

```python
def __eq__(self, other):
    return self.name == other.name
```

Defines logical equality.

---

# 10. Identity vs Equality

Important distinction:

```python
item1 == item2
```

Uses `__eq__`

But:

```python
item1 is item2
```

Checks memory identity.

Two objects can be equal but not identical.

---

# 11. How Magic Methods Integrate with Python Data Model

Python’s data model is built around magic methods.

When you do:

```
a + b
```

Python internally does:

```
a.__add__(b)
```

When you do:

```
len(a)
```

Python does:

```
a.__len__()
```

Understanding this unlocks full Python power.

---

# 12. Overriding Behavior Carefully

Magic methods should:

* Be predictable
* Follow expected semantics
* Not violate user intuition

Example bad practice:

```python
def __add__(self, other):
    return "Hello"
```

Confusing and misleading.

Follow logical consistency.

---

# 13. `__repr__` in Large Systems

In large applications:

* Logging relies on `__repr__`
* Debuggers rely on `__repr__`
* Testing output relies on `__repr__`

Poor representation makes debugging painful.

---

# 14. Performance Considerations

Keep `__repr__`:

* Lightweight
* Fast
* Free of heavy computations

It should not:

* Query database
* Perform network calls
* Modify state

Representation should be pure.

---

# 15. Common Interview Questions

Q: Difference between `__str__` and `__repr__`?

Q: What happens if only `__repr__` exists?

Q: Why return recreatable string in `__repr__`?

Q: How does `+` operator work internally?

Q: What is descriptor protocol relation to methods?

---

# 16. Advanced Insight – Everything is Hookable

Because of magic methods:

You can customize:

* Arithmetic
* Comparison
* Container behavior
* Context manager behavior
* Iteration

Python becomes extremely flexible.

---

# 17. Design Philosophy for Magic Methods

Use them to:

* Integrate cleanly
* Make objects intuitive
* Improve readability

Do not use them to:

* Hide logic
* Confuse users
* Break conventions

---

# 18. Key Takeaways

* Magic methods integrate classes with Python’s core behavior.
* `__repr__` is essential for debugging.
* `__str__` is for user-friendly display.
* Operator overloading works through magic methods.
* Identity (`is`) is different from equality (`==`).
* Clean representation improves maintainability.

Mastering magic methods makes your classes feel native to Python.

