# 02 – Constructors and Object Lifecycle 

This section goes beyond surface-level understanding of `__init__`.

We will understand:

* What actually happens during object creation
* Difference between `__new__` and `__init__`
* How memory allocation works conceptually
* Constructor execution flow
* Parameter binding mechanics
* Default values and mutability traps
* Type hints vs runtime validation
* Defensive programming patterns
* Object lifecycle stages
* Garbage collection basics
* Common interview traps

---

# 1. What Happens When You Create an Object?

When you write:

```python
item1 = Item("Phone", 100, 5)
```

Python performs multiple internal steps.

## Step-by-step breakdown:

1. The class `Item` is called.
2. Python executes `Item.__new__()` first.
3. Memory is allocated for a new object.
4. A blank instance is created.
5. Python then calls `Item.__init__()`.
6. The instance is initialized with given arguments.
7. The reference is stored in `item1`.

Important:

* `__new__` creates the object.
* `__init__` initializes the object.

Most developers only use `__init__`, but knowing this difference is important for advanced cases.

---

# 2. `__new__` vs `__init__`

## `__new__`

* Static method.
* Responsible for creating the instance.
* Rarely overridden unless dealing with immutables or metaclasses.

Example:

```python
class Item:
    def __new__(cls, *args, **kwargs):
        print("Allocating memory")
        return super().__new__(cls)

    def __init__(self, name, price):
        print("Initializing object")
        self.name = name
        self.price = price
```

Execution order:

```
Allocating memory
Initializing object
```

Key insight:
If `__new__` does not return an instance, `__init__` will not run.

---

# 3. Constructor (`__init__`) Deep Understanding

Basic structure:

```python
class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
```

Key properties:

* Automatically called after object creation.
* Must return `None`.
* Used to initialize instance attributes.

If you try to return something else:

```python
def __init__(self):
    return "something"
```

You get:

```
TypeError: __init__() should return None
```

---

# 4. Parameter Binding Mechanics

When calling:

```python
item1 = Item("Phone", 100, 5)
```

Internally Python binds:

* self → newly created instance
* name → "Phone"
* price → 100
* quantity → 5

Binding follows Python's standard function rules:

* Positional arguments
* Keyword arguments
* Default arguments
* *args
* **kwargs

Example:

```python
item1 = Item(name="Phone", price=100)
```

Works because quantity has default value.

---

# 5. Default Parameters and Mutable Trap

Dangerous example:

```python
class Example:
    def __init__(self, items=[]):
        self.items = items
```

Problem:

Default mutable arguments are shared across instances.

Correct approach:

```python
class Example:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items
```

This is a common interview question.

---

# 6. Type Hints vs Runtime Validation

Type hints:

```python
def __init__(self, name: str, price: float):
```

Important:

* They are not enforced at runtime.
* They are annotations.

If someone passes wrong type, Python will not stop execution.

Therefore we use validation.

---

# 7. Defensive Programming in Constructors

Validation using `assert`:

```python
assert price >= 0, f"Price {price} must be >= 0"
assert quantity >= 0, f"Quantity {quantity} must be >= 0"
```

Why validation is critical:

* Prevent corrupted object state.
* Fail fast principle.
* Avoid hidden downstream bugs.

Better approach for production:

```python
if price < 0:
    raise ValueError("Price cannot be negative")
```

Assertions can be disabled with optimization flags.

---

# 8. Dynamic Attribute Assignment

Inside constructor:

```python
self.name = name
```

This creates entry in:

```python
self.__dict__
```

Example:

```python
print(item1.__dict__)
```

Output:

```
{'name': 'Phone', 'price': 100, 'quantity': 5}
```

This is how Python stores instance attributes internally.

---

# 9. Object Lifecycle Stages

Complete lifecycle:

1. Class definition (loaded into memory)
2. Object creation (`__new__`)
3. Initialization (`__init__`)
4. Usage phase
5. Dereferencing
6. Garbage collection

---

# 10. Garbage Collection Basics

Python uses:

* Reference counting
* Cyclic garbage collector

When reference count becomes zero:

Object becomes eligible for deletion.

Example:

```python
item1 = Item("Phone", 100)
del item1
```

If no references remain → object cleaned.

---

# 11. `__del__` Destructor

```python
class Item:
    def __del__(self):
        print("Object destroyed")
```

Not recommended for critical logic.

Reasons:

* Not guaranteed execution timing.
* GC behavior may delay destruction.

Use context managers instead for resource handling.

---

# 12. Constructor Best Practices

1. Keep constructor simple.
2. Validate inputs early.
3. Avoid heavy computation.
4. Avoid I/O operations inside constructor.
5. Do not mutate global state.
6. Avoid complex branching logic.

Constructor should establish valid object state.

---

# 13. Common Interview Questions

Q1: Difference between `__new__` and `__init__`?

Q2: Why can’t `__init__` return a value?

Q3: What happens if constructor raises exception?

* Object creation fails.
* Partially constructed object discarded.

Q4: What is mutable default argument trap?

Q5: How does Python manage memory?

---

# 14. Mental Model for Strong OOP

Constructor is not just for assigning values.

It is responsible for:

* Establishing invariants
* Protecting object integrity
* Preventing invalid states
* Preparing object for safe usage

A well-designed constructor prevents 70% of runtime bugs.

---

# 15. Key Takeaways

* `__new__` creates, `__init__` initializes.
* Constructor must return None.
* Default mutable arguments are dangerous.
* Type hints are not enforcement.
* Validation is mandatory in real systems.
* Objects have a lifecycle.
* Garbage collection is automatic but not magical.

This level of understanding separates beginner OOP from professional OOP.

