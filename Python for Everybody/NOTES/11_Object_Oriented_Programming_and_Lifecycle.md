# Object Oriented Programming and Object Lifecycle

Focus:

* Core OOP pillars
* Python-specific object model
* Memory management
* Object lifecycle
* Advanced interview questions

---

# 1. Why Object Oriented Programming?

OOP is a paradigm for structuring programs using objects.

An object:

* Encapsulates data (state)
* Encapsulates behavior (methods)

Why OOP?

* Modularity
* Reusability
* Maintainability
* Scalability

In large systems, procedural code becomes hard to manage.
OOP helps model real-world entities and system components.

---

# 2. Class vs Object

Class:
Blueprint or template.

Object:
Instance of class.

Example:

class Person:
pass

p = Person()

Memory is allocated when object is created, not when class is defined.

Interview Question:
When is memory allocated for a class?
Class definition creates class object.
Instance memory allocated when instantiated.

---

# 3. The Four Pillars of OOP

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

---

# 4. Encapsulation

Encapsulation = Bundling data and methods together.

Python uses naming conventions:

_public
_protected (convention only)
__private (name mangling)

Example:

class BankAccount:
def **init**(self, balance):
self.__balance = balance

```
def deposit(self, amount):
    self.__balance += amount
```

Name mangling changes:
__balance → _ClassName__balance

Important:
Python does not enforce strict private access.
It relies on convention.

---

# 5. Abstraction

Abstraction = Hiding implementation details.

In Python:
Use abstract base classes.

from abc import ABC, abstractmethod

class Shape(ABC):
@abstractmethod
def area(self):
pass

Abstract classes cannot be instantiated.

Interview Question:
Why use abstraction?
To define contract without enforcing implementation details.

---

# 6. Inheritance

Inheritance allows a class to acquire properties of another.

class Animal:
def speak(self):
print("Sound")

class Dog(Animal):
def speak(self):
print("Bark")

Types:

* Single
* Multiple
* Multilevel
* Hierarchical

Python supports multiple inheritance.

---

# 7. Method Resolution Order (MRO)

In multiple inheritance, Python uses C3 linearization.

Check MRO:

ClassName.**mro**

Interview Question:
How does Python resolve method in multiple inheritance?
Uses C3 linearization algorithm.

---

# 8. Polymorphism

Same interface, different behavior.

Example:

class Cat:
def speak(self):
return "Meow"

class Dog:
def speak(self):
return "Bark"

for animal in [Cat(), Dog()]:
print(animal.speak())

This is duck typing.

"If it behaves like a duck, treat it like a duck."

Python relies on dynamic typing.

---

# 9. Special Methods (Dunder Methods)

Python objects implement special methods.

Examples:

**init**  → constructor
**new**   → object creation
**str**   → user-friendly string
**repr**  → developer representation
**len**   → length
**add**   → operator overloading

Example:

class Vector:
def **init**(self, x, y):
self.x = x
self.y = y

```
def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)
```

Operator overloading uses dunder methods.

---

# 10. Object Lifecycle (Critical Interview Topic)

Object lifecycle stages:

1. Creation
2. Initialization
3. Usage
4. Destruction

---

# 11. **new** vs **init**

**new**:

* Allocates memory
* Returns new instance
* Static method

**init**:

* Initializes instance
* Runs after **new**

Flow:

obj = Class()

Step 1: **new** called
Step 2: **init** called

Interview Question:
When override **new**?
When controlling instance creation (e.g., Singleton).

---

# 12. Memory Management in Python

Python uses:

* Reference counting
* Garbage collection (cyclic GC)

Reference count increases when:

* New variable points to object

Decreases when:

* Variable deleted
* Goes out of scope

When reference count = 0:
Object eligible for destruction.

---

# 13. Garbage Collector

Reference counting cannot handle circular references.

Example:
A → B
B → A

GC detects unreachable cycles and removes them.

Python uses generational GC:

* Young generation
* Middle generation
* Old generation

Objects surviving multiple cycles move to older generation.

---

# 14. Destructor (**del**)

**del** is called when object is about to be destroyed.

Not guaranteed execution timing.
Avoid relying on it for critical cleanup.

Better approach:
Use context managers.

---

# 15. Context Managers and Resource Management

Used for:

* Files
* Database connections
* Network sockets

Implemented using:
**enter**
**exit**

Example:

class FileHandler:
def **enter**(self):
print("Opening resource")
return self

```
def __exit__(self, exc_type, exc_val, exc_tb):
    print("Closing resource")
```

Ensures deterministic cleanup.

---

# 16. Composition vs Inheritance

Inheritance:
"is-a" relationship.

Composition:
"has-a" relationship.

Prefer composition over inheritance when possible.

Why?
More flexible.
Looser coupling.

---

# 17. SOLID Principles (High-Level)

S — Single Responsibility
O — Open/Closed
L — Liskov Substitution
I — Interface Segregation
D — Dependency Inversion

Interview relevance:
Demonstrates design maturity.

---

# 18. Class vs Static Methods

Instance method:
Requires object.

@classmethod:
Receives class as first parameter.

@staticmethod:
No access to class or instance.

Use case:
Factory methods often use @classmethod.

---

# 19. Immutable vs Mutable Objects

Mutable:
List, dict, set

Immutable:
int, float, str, tuple

Important for:

* Performance
* Thread safety
* Hashability

---

# 20. Common Interview Questions

1. Difference between **new** and **init**?
   **new** creates instance.
   **init** initializes it.

2. How does Python manage memory?
   Reference counting + cyclic GC.

3. What is MRO?
   Order in which base classes are searched.

4. What is duck typing?
   Behavior-based polymorphism.

5. Why avoid deep inheritance chains?
   Increases complexity and tight coupling.

6. When use composition?
   When relationship is not strictly "is-a".

---

# Final Understanding

OOP in Python is flexible and dynamic.
Object lifecycle involves creation, initialization, usage, and destruction.
Memory management is automatic but not magical.
Understanding MRO, dunder methods, and lifecycle is crucial for backend and system design interviews.
Mastering these concepts means you understand Python beyond surface syntax.

