# 07 – Inheritance and Code Reusability

Inheritance is one of the most powerful — and most misused — features of OOP.

In this section we go far beyond:

* "Child class inherits parent"

We will understand:

* What inheritance actually means internally
* How Python’s Method Resolution Order (MRO) works
* Constructor chaining with `super()`
* Method overriding mechanics
* Class attribute overriding
* Polymorphic behavior through inheritance
* When inheritance is a bad idea
* Composition vs inheritance (architecture decision)

This is core interview-level material.

---

# 1. What is Inheritance?

Inheritance allows a class (child) to reuse logic from another class (parent).

Basic syntax:

```python
class Phone(Item):
    pass
```

This means:

* Phone gets all attributes and methods of Item
* Phone can extend or override behavior

Conceptually:

Phone **is a** type of Item.

---

# 2. Why Inheritance Exists

Without inheritance:

You would copy-paste code.

Example bad design:

```python
class Phone:
    # duplicate Item code here

class Keyboard:
    # duplicate Item code again
```

Problems:

* Code duplication
* Hard to maintain
* Bug fixes must be repeated

Inheritance solves this.

---

# 3. Inheriting Constructor Behavior

If parent has constructor:

```python
class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
```

Child automatically inherits it.

```python
phone1 = Phone("iPhone", 1000, 5)
```

Works because Phone inherits `__init__`.

---

# 4. Extending Constructor (Constructor Chaining)

What if Phone needs extra attribute?

Example:

```python
class Phone(Item):
    def __init__(self, name, price, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones
```

Important:

`super().__init__()` calls parent constructor.

Without it:

Parent attributes would not be initialized.

---

# 5. What `super()` Actually Does

`super()` does NOT mean "parent class directly".

It means:

Follow MRO (Method Resolution Order).

In simple inheritance:

MRO = [Phone, Item, object]

So:

```python
super()
```

Inside Phone refers to Item.

---

# 6. Method Overriding

Child can redefine parent method.

Example:

```python
class Item:
    def calculate_total_price(self):
        return self.price * self.quantity

class Phone(Item):
    def calculate_total_price(self):
        return (self.price * self.quantity) - 10
```

Phone overrides behavior.

This is polymorphism in action.

---

# 7. Calling Parent Method from Overridden Method

Sometimes you extend, not replace.

```python
class Phone(Item):
    def calculate_total_price(self):
        base_total = super().calculate_total_price()
        return base_total - 10
```

This is safe extension.

---

# 8. Method Resolution Order (MRO)

Python determines method lookup using MRO.

Check MRO:

```python
print(Phone.mro())
```

Output example:

```
[Phone, Item, object]
```

Lookup order:

1. Child class
2. Parent class
3. object

This matters when methods exist in multiple places.

---

# 9. Multiple Inheritance (Advanced)

Python supports multiple inheritance.

Example:

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

MRO becomes more complex.

Python uses C3 linearization algorithm.

Interview-level awareness required.

---

# 10. Class Attribute Overriding

Parent:

```python
class Item:
    pay_rate = 0.8
```

Child override:

```python
class Phone(Item):
    pay_rate = 0.7
```

Now:

Phone instances use 0.7
Item instances use 0.8

This is class-level polymorphism.

---

# 11. Polymorphism via Inheritance

Example:

```python
items = [Item("A", 100, 1), Phone("B", 200, 2)]

for item in items:
    print(item.calculate_total_price())
```

Different behavior depending on object type.

Same interface.

Different implementation.

---

# 12. When NOT to Use Inheritance

Inheritance should model:

"is-a" relationship.

Bad example:

Car inherits from Engine.

Car is NOT an Engine.
Car HAS an Engine.

This is composition, not inheritance.

---

# 13. Composition vs Inheritance

Composition example:

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
```

Car has an Engine.

Composition is often safer.

Inheritance creates tight coupling.

---

# 14. Tight Coupling Problem

If parent class changes,
All child classes affected.

Deep inheritance trees become fragile.

Best practice:

Keep inheritance shallow.

---

# 15. Open/Closed Principle

Good inheritance allows:

* Extending behavior
* Without modifying parent code

Phone extends Item without changing Item.

This is Open/Closed Principle.

---

# 16. Constructor Execution Order

When creating Phone object:

1. Phone.**new**
2. Phone.**init**
3. Inside it → super().**init**
4. Item.**init** executes

Initialization flows upward via MRO.

---

# 17. Common Mistakes

* Forgetting `super()`
* Duplicating parent code
* Overusing inheritance
* Breaking Liskov Substitution Principle

---

# 18. Liskov Substitution Principle (Important)

Objects of child class should be replaceable for parent class.

If Item expects certain behavior,
Phone should not break it.

Violating this breaks polymorphism.

---

# 19. Interview-Level Questions

Q: What is MRO?

Q: What happens if method exists in both parent and child?

Q: Why use `super()` instead of parent class name?

Q: What is diamond problem?

Q: What is C3 linearization?

---

# 20. Key Takeaways

* Inheritance enables code reuse.
* Child classes extend or override behavior.
* `super()` follows MRO.
* Keep inheritance shallow.
* Prefer composition when relationship is "has-a".
* Understand MRO for debugging.
* Design inheritance carefully to avoid tight coupling.

Mastering inheritance is essential for scalable architecture.

