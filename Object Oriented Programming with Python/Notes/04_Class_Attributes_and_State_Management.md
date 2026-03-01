# 04 – Class Attributes and State Management

This section is where OOP maturity actually begins.

Most beginners understand instance attributes.
Very few truly understand:

* Class attributes
* Shared state problems
* Attribute resolution order
* Shadowing behavior
* Mutation risks
* Internal storage model
* When to use class attributes vs instance attributes
* How to design global state safely

We are going to go extremely deep.

---

# 1. Instance Attributes vs Class Attributes (Core Difference)

## Instance Attribute

Defined inside constructor:

```python
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

Stored inside:

```
instance.__dict__
```

Each object gets its own copy.

---

## Class Attribute

Defined directly inside class:

```python
class Item:
    pay_rate = 0.8
```

Stored inside:

```
Item.__dict__
```

Shared across ALL instances.

Important mental model:

Instance attributes → per object state
Class attributes → shared state

---

# 2. Attribute Lookup Order (Critical Concept)

When you access:

```python
item1.pay_rate
```

Python searches in this order:

1. item1.**dict**
2. Item.**dict**
3. Parent classes (MRO order)

This is called the **attribute resolution chain**.

Example:

```python
class Item:
    pay_rate = 0.8

item1 = Item()
print(item1.pay_rate)
```

Output:

```
0.8
```

Even though `pay_rate` is NOT inside `item1.__dict__`.

---

# 3. Inspecting Internal Storage with `__dict__`

Check instance dictionary:

```python
print(item1.__dict__)
```

Output:

```
{}
```

Check class dictionary:

```python
print(Item.__dict__)
```

You will see:

```
{'pay_rate': 0.8, ...}
```

This proves:

The attribute exists only at class level.

---

# 4. Shadowing (Overriding Class Attribute at Instance Level)

Now watch carefully:

```python
item1.pay_rate = 0.7
```

What happens?

Python creates a NEW attribute inside instance.

Now:

```python
print(item1.__dict__)
```

Output:

```
{'pay_rate': 0.7}
```

But:

```python
print(Item.pay_rate)
```

Still:

```
0.8
```

This is called **shadowing**.

The instance attribute overrides class attribute only for that object.

---

# 5. Why Access via `self` Instead of Class Name

Bad design:

```python
self.price = self.price * Item.pay_rate
```

Better design:

```python
self.price = self.price * self.pay_rate
```

Why?

Because if instance overrides `pay_rate`,
`self.pay_rate` will respect that override.

Hardcoding class name ignores shadowing.

---

# 6. Shared Mutable State Problem

Dangerous example:

```python
class Item:
    all_items = []
```

This list is SHARED across all instances.

Example:

```python
item1 = Item()
item2 = Item()

item1.all_items.append("Phone")

print(item2.all_items)
```

Output:

```
['Phone']
```

Because it is shared memory.

Important:

Mutable class attributes create shared mutation side effects.

---

# 7. Registry Pattern (Correct Usage of Class Attribute)

In the store system, we used:

```python
class Item:
    all = []
```

And inside constructor:

```python
Item.all.append(self)
```

This is intentional shared state.

This is called a **registry pattern**.

Purpose:

Track all instances created.

This is a correct use case for shared mutable class attribute.

---

# 8. When NOT to Use Class Attributes

Do NOT use class attributes for:

* User-specific data
* Per-instance state
* Changing runtime values frequently

Example mistake:

```python
class Item:
    price = 0
```

Now every instance shares same price unless shadowed.

This creates confusion.

---

# 9. Class Attributes and Inheritance

Example:

```python
class Item:
    pay_rate = 0.8

class Phone(Item):
    pass
```

Now:

```python
print(Phone.pay_rate)
```

Output:

```
0.8
```

Inheritance copies attribute lookup access.

Now override:

```python
class Phone(Item):
    pay_rate = 0.7
```

Now:

```python
print(Phone.pay_rate)
```

Output:

```
0.7
```

But:

```python
print(Item.pay_rate)
```

Still:

```
0.8
```

This is polymorphic behavior.

---

# 10. Class Attribute vs Global Variable

Difference:

Global variable:

* Exists independently
* Hard to track
* Poor encapsulation

Class attribute:

* Namespaced
* Belongs to class conceptually
* Cleaner design

Prefer class attribute over global state.

---

# 11. Dynamic Class Attribute Modification

You can change class attribute dynamically:

```python
Item.pay_rate = 0.9
```

Now ALL instances (without shadowing) reflect new value.

This can be powerful or dangerous.

Be careful.

---

# 12. State Management Strategies

Good architecture requires deciding:

* What is shared?
* What is per-instance?
* What is constant?

Examples:

Shared across store:

* Tax rate
* Default discount

Per-instance:

* Name
* Price
* Quantity

Constant:

* Category type

---

# 13. Memory Model Insight

Instance:

```
item1 -> reference
         |
         v
     object in heap
         |
     __dict__
```

Class:

```
Item -> class object
         |
     __dict__
```

Class object also lives in memory.

Instances reference class internally.

That is how lookup chain works.

---

# 14. Class State vs Instance State Bugs

Common bug:

Accidentally modifying class attribute inside instance.

Example:

```python
self.pay_rate = self.pay_rate - 0.1
```

If `pay_rate` was intended global, this shadows it.

Better:

```python
Item.pay_rate = Item.pay_rate - 0.1
```

Know your intention.

---

# 15. Advanced: Using `@classmethod` to Modify Class State

Example:

```python
@classmethod
def set_pay_rate(cls, new_rate):
    cls.pay_rate = new_rate
```

Now change class state safely.

---

# 16. Interview-Level Questions

Q: What happens if instance and class both define same attribute?

Instance wins.

Q: Where are class attributes stored?

Inside class `__dict__`.

Q: Are class attributes copied into instances?

No. They are looked up dynamically.

Q: What is shadowing?

Overriding class attribute at instance level.

---

# 17. Architecture Design Principle

Ask before defining attribute:

* Does this belong to object?
* Or does it belong to concept of class?

Wrong classification creates messy architecture.

---

# 18. Key Takeaways

* Class attributes are shared state.
* Instance attributes are per-object state.
* Lookup order: instance → class → parent.
* Shadowing overrides locally.
* Mutable class attributes are dangerous.
* Registry pattern is valid use case.
* Proper state management defines scalable design.

Understanding this deeply prevents 50% of OOP bugs in real systems.

