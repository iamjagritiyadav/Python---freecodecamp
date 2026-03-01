# 03 – Methods and Class Architecture

This section is not just about writing methods.

It is about understanding:

* How methods are bound to objects
* What actually happens when you call a method
* Difference between instance, class, and static methods
* Method binding mechanics internally
* Architectural decisions while designing classes
* When to use what type of method
* How to structure behavior in scalable systems

We move from syntax → to internal mechanics → to architecture thinking.

---

# 1. What is a Method Really?

A method is just a function defined inside a class.

Example:

```python
class Item:
    def calculate_total_price(self):
        return self.price * self.quantity
```

Important conceptual shift:

When you define a function inside a class, it becomes a *descriptor*.

It does not immediately become "bound" to any object.

Binding happens during access.

---

# 2. What Happens When You Call a Method?

When you write:

```python
item1.calculate_total_price()
```

Python internally converts it to:

```python
Item.calculate_total_price(item1)
```

That means:

* The instance (`item1`) is passed automatically.
* That instance becomes `self`.

This is called **method binding**.

---

# 3. Bound vs Unbound Methods

If you access the method from the class:

```python
Item.calculate_total_price
```

You get an unbound function.

If you access it from the instance:

```python
item1.calculate_total_price
```

You get a bound method.

You can verify:

```python
print(item1.calculate_total_price)
```

Output will show something like:

```
<bound method Item.calculate_total_price of <Item object>>
```

This means:

* The function is now attached to that specific object.

---

# 4. Why `self` Exists (Internal Mechanics)

If you remove `self`:

```python
def calculate_total_price():
    pass
```

Calling from instance gives:

```
TypeError: takes 0 positional arguments but 1 was given
```

Because Python always injects the instance automatically.

Important:

`self` is NOT a keyword.
It is a naming convention.

But breaking the convention makes your code unreadable.

---

# 5. Designing Instance Methods Properly

An instance method:

* Works on instance data
* Modifies instance state
* Reads instance attributes

Example:

```python
class Item:
    def apply_discount(self):
        self.price = self.price * self.pay_rate
```

This modifies internal state.

Architecture rule:

If a method needs instance data → it should be an instance method.

---

# 6. Class Methods (`@classmethod`)

Class methods receive the class itself as first argument.

Example:

```python
class Item:

    @classmethod
    def instantiate_from_csv(cls):
        print(cls)
```

Calling:

```python
Item.instantiate_from_csv()
```

Internally:

```python
Item.instantiate_from_csv(Item)
```

`cls` refers to the class object.

---

# 7. When to Use Class Methods

Use case:

Alternative constructors.

Example:

```python
@classmethod
def from_string(cls, data_str):
    name, price = data_str.split(",")
    return cls(name, float(price))
```

Now:

```python
item1 = Item.from_string("Phone,100")
```

Why not static method?

Because:

* You want to create instance of the class.
* If subclass calls this method, `cls` ensures correct subclass instantiation.

This is critical for inheritance.

---

# 8. Static Methods (`@staticmethod`)

Static methods:

* Do not receive instance
* Do not receive class
* Behave like regular functions
* Live inside class namespace

Example:

```python
@staticmethod
def is_integer(num):
    if isinstance(num, float):
        return num.is_integer()
    elif isinstance(num, int):
        return True
    return False
```

Calling:

```python
Item.is_integer(5)
```

No automatic argument injection.

---

# 9. Class Method vs Static Method (Architectural Difference)

| Feature                 | Instance Method | Class Method | Static Method |
| ----------------------- | --------------- | ------------ | ------------- |
| Receives instance       | Yes             | No           | No            |
| Receives class          | No              | Yes          | No            |
| Modifies instance state | Yes             | Rarely       | No            |
| Alternative constructor | No              | Yes          | No            |
| Utility helper          | Sometimes       | Rarely       | Yes           |

Architectural thinking:

* Needs instance? → instance method
* Needs class-level logic? → class method
* Pure utility tied conceptually to class? → static method

---

# 10. Method Resolution and Lookup

When calling:

```python
item1.apply_discount()
```

Python searches in order:

1. Instance dictionary
2. Class dictionary
3. Parent classes (MRO order)

This becomes critical when inheritance enters.

---

# 11. Internal View of Methods (Descriptor Protocol Insight)

Functions inside class implement descriptor protocol.

When accessed via instance:

Python calls:

```
function.__get__(instance, owner_class)
```

This produces bound method.

This is advanced but important for interviews.

---

# 12. Architectural Decisions While Designing Classes

Common beginner mistake:

Putting too much logic inside constructor.

Better approach:

* Constructor → setup
* Methods → behavior

Another mistake:

Using too many static methods.

If most methods are static, maybe you don’t need a class.

---

# 13. Cohesion Principle

A class should represent one concept.

Example:

Item class should:

* Store item data
* Manage item-related behavior

It should NOT:

* Handle database logic
* Handle UI logic
* Handle unrelated operations

This is high cohesion principle.

---

# 14. Example Architecture: Store System

Good separation:

* Item class → item behavior
* Phone class → phone-specific logic
* CSV loader → class method
* Price validation → constructor
* Discount logic → instance method

This separation prevents tight coupling.

---

# 15. Common Interview Traps

Q: Why is `self` required?

Q: What happens if you call instance method from class?

Example:

```python
Item.calculate_total_price(item1)
```

Works because you pass instance manually.

Q: Why use `cls` in class methods instead of class name?

Answer:
To support inheritance properly.

Q: Can static methods access class attributes?

Only by explicitly referencing class name.

---

# 16. Advanced Design Thought

Ask before writing method:

* Does it depend on instance state?
* Does it depend on class state?
* Is it just a helper?

Bad design example:

Making every method static.

Bad design example:

Accessing class attributes via class name inside instance method instead of `self`.

Better approach:

Use `self.attribute` so instance-level overrides work.

---

# 17. Method Call Stack Visualization

Example call:

```python
item1.apply_discount()
```

Call stack:

1. Python resolves attribute `apply_discount`
2. Binds instance
3. Pushes function frame
4. Executes method body
5. Updates instance state
6. Returns control

Understanding this prevents confusion.

---

# 18. Key Takeaways

* Methods are functions stored in class namespace.
* Binding happens during access.
* Instance methods receive `self`.
* Class methods receive `cls`.
* Static methods receive nothing automatically.
* Proper class architecture separates responsibilities.
* Good design reduces future bugs.

Strong OOP is about architecture, not syntax.

