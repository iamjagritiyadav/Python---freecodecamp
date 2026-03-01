# 06 – Data Integration and Class Methods (Production-Level Thinking)

This section moves from "learning OOP" → to "building real systems".

Until now, we manually created objects like this:

```python
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
```

This works for 2–5 objects.

It does NOT work for:

* 500 products
* External datasets
* Database-driven systems
* API-based systems

Real applications do not hardcode data.

They integrate with external sources.

This is where **class methods** become powerful.

---

# 1. The Real Problem: Hardcoded Data

Hardcoding inside main file:

```python
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
```

Problems:

* Data mixed with logic
* Not scalable
* Not reusable
* Hard to update
* Not production-ready

Better architecture:

Separate:

* Data layer
* Business logic layer

---

# 2. Why CSV is Used in the Course

CSV = Comma Separated Values.

Example:

```
name,price,quantity
Phone,100,5
Laptop,1000,3
Keyboard,75,10
```

Why CSV?

* Simple
* Human readable
* Table structured
* Easily parsed
* No database setup required

This simulates real-world data ingestion.

---

# 3. Reading CSV in Python

```python
import csv

with open('items.csv', 'r') as f:
    reader = csv.DictReader(f)
    items = list(reader)
```

`DictReader` converts rows into dictionaries:

```
{'name': 'Phone', 'price': '100', 'quantity': '5'}
```

Important:

Values are strings by default.

---

# 4. Why Class Method is Needed Here

If we write this logic in main file:

```python
for data in items:
    Item(data['name'], int(data['price']), int(data['quantity']))
```

This breaks OOP principles.

Reason:

Object creation logic should belong to class.

Not to main file.

So we use:

```python
@classmethod
```

---

# 5. What is a Class Method Really?

```python
@classmethod
def instantiate_from_csv(cls):
```

Key differences from instance method:

* Receives class as first argument
* No instance required
* Used to create instances

Internally:

```python
Item.instantiate_from_csv()
```

Becomes:

```python
Item.instantiate_from_csv(Item)
```

`cls` refers to class object.

---

# 6. Full CSV Factory Method Implementation

```python
@classmethod
def instantiate_from_csv(cls):
    with open('items.csv', 'r') as f:
        reader = csv.DictReader(f)
        items = list(reader)

    for item in items:
        cls(
            name=item.get('name'),
            price=float(item.get('price')),
            quantity=int(item.get('quantity'))
        )
```

Why `cls()` instead of `Item()`?

Because:

Inheritance safe design.

If subclass calls this method:

```python
Phone.instantiate_from_csv()
```

`cls` will refer to `Phone`, not `Item`.

This is advanced design thinking.

---

# 7. Type Conversion Problems

CSV values are strings.

If you forget conversion:

```python
price=item.get('price')
```

Then multiplication:

```python
"100" * 3
```

Result:

```
100100100
```

String repetition instead of arithmetic.

This is a subtle but dangerous bug.

Always convert explicitly:

```python
float()
int()
```

---

# 8. Validation During Data Import

Constructor already has validation:

```python
assert price >= 0
```

If CSV contains negative value:

Object creation fails immediately.

This is defensive design.

Never trust external data.

---

# 9. Central Registry Pattern

Earlier we created:

```python
class Item:
    all = []
```

Inside constructor:

```python
Item.all.append(self)
```

Now when class method creates instances,

They automatically register.

So after:

```python
Item.instantiate_from_csv()
```

We can:

```python
print(Item.all)
```

This gives list of all objects.

Clean architecture.

---

# 10. Why Not Use Static Method?

Because static method:

* Does not receive class
* Cannot instantiate safely with inheritance

Bad design:

```python
@staticmethod
def instantiate():
    return Item(...)
```

If subclass calls it, it still returns Item.

Breaks polymorphism.

---

# 11. Separation of Concerns Principle

Correct architecture:

* CSV parsing inside class method
* Object validation inside constructor
* Business logic inside instance methods

Wrong architecture:

* Everything inside main file

---

# 12. Extending to Other Data Sources

Same pattern works for:

* JSON
* Database
* API response
* YAML

Example:

```python
@classmethod
def from_json(cls, file_path):
    pass
```

Factory pattern in action.

---

# 13. Error Handling in Production

Better version:

```python
try:
    price = float(item.get('price'))
except ValueError:
    raise ValueError("Invalid price format")
```

Never assume external file is correct.

---

# 14. Architecture Comparison

Beginner approach:

```
main.py handles everything
```

Professional approach:

```
Item class handles its own instantiation logic
main.py only orchestrates
```

---

# 15. Interview-Level Insight

Q: Why use class method instead of constructor directly?

Because constructor handles one object.
Class method handles bulk structured instantiation.

Q: Why use `cls` instead of class name?

Supports inheritance and polymorphism.

Q: What pattern is this?

Factory pattern.

---

# 16. Factory Pattern Concept

Factory method:

Encapsulates object creation logic.

Advantages:

* Cleaner code
* Centralized logic
* Scalable
* Extendable

---

# 17. Real-World Thinking

Imagine:

Tomorrow your system reads from database.

You only change factory method.

Constructor stays untouched.

Instance methods stay untouched.

Architecture stable.

---

# 18. Key Takeaways

* Never hardcode bulk data.
* Use class methods for structured instantiation.
* Always convert external data types.
* Validate external data.
* Use `cls()` not class name.
* Registry pattern helps track instances.
* Class methods are foundation of scalable design.

This is where OOP transitions from academic to production-grade engineering.

