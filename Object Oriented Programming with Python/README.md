# Object Oriented Programming with Python

This folder contains my notes and implementation code from the **Object Oriented Programming with Python** course.

The content is based on the full OOP course taught by **Jim (JimShapedCoding)** on the freeCodeCamp channel.

Course code reference: https://github.com/jimdevops19/PythonOOP  

All credit for the original teaching and explanations goes to him.

---

## Topics Covered

### Getting Started with Classes
- Why OOP matters in real-world software development
- Classes vs objects
- Creating custom data types
- Instance creation and attribute assignment
- Understanding that everything in Python is an object

### Constructors and Object Initialization
- `__init__` method (constructor)
- Automatic execution during instantiation
- Dynamic attribute assignment
- Default parameter values
- Type hints for parameters
- Input validation using `assert`
- Best practices for clean initialization

### Instance Attributes vs Class Attributes
- Difference between instance-level and class-level attributes
- Shared state across objects
- Attribute lookup order (instance → class)
- Overriding class attributes per instance
- `__dict__` inspection and debugging

### Methods and Object Behavior
- Defining methods inside classes
- The role of `self`
- Accessing instance attributes inside methods
- Applying discounts and modifying internal state
- Best practices for accessing class attributes from instances

### Magic Methods (Dunder Methods)
- `__init__`
- `__repr__` for developer-friendly representation
- Proper object representation for debugging
- Best practices for recreatable object representations

### Class Methods
- `@classmethod` decorator
- `cls` parameter behavior
- Alternative constructors
- Instantiating objects from structured data
- Reading from CSV files
- Structured data instantiation patterns

### Static Methods
- `@staticmethod` decorator
- When to use static methods
- Logical grouping vs instance dependency
- Differences between static and class methods

### Managing External Data (CSV Integration)
- Separating data from logic
- Using `csv.DictReader`
- Converting strings to `int` and `float`
- Instantiating multiple objects dynamically
- Maintaining a centralized object registry (`all` list)

### Inheritance
- Parent vs child classes
- Code reuse across classes
- Overriding behavior in child classes
- Using `super()` correctly
- Extending constructors safely
- Avoiding duplication in subclasses

### Encapsulation
- Restricting direct attribute access
- Private attributes (`__attribute`)
- Read-only attributes using `@property`
- Getters and setters
- Controlled mutation of internal state
- Validating updates before assignment

### Abstraction
- Hiding internal implementation details
- Private methods
- Separating public APIs from internal processes
- Designing clean class interfaces

### Polymorphism
- Same method, different behavior
- Method overriding
- Built-in polymorphism (`len()` example)
- Applying polymorphism across inherited classes
- Shared interfaces across multiple child classes

### Project Structure & Code Organization
- Splitting classes into separate files
- Proper imports between modules
- Keeping `main.py` clean
- Scalable project architecture

### OOP Principles
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

---

## Practical Implementation

Throughout this module, a **Store Management System** is developed step-by-step to demonstrate:

- Object modeling
- Scalable class design
- Data validation strategies
- Controlled attribute management
- Inheritance-based system extension
- Clean separation of data and logic

---

## What This Module Strengthens

- Strong conceptual clarity of OOP
- Writing scalable Python applications
- Designing maintainable class architectures
- Preparing for backend development roles
- Interview-level understanding of object-oriented design

---

This module is part of a structured effort to complete the entire freeCodeCamp Python playlist and build a strong Python foundation from beginner to advanced level.
