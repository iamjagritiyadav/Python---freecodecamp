#  Variables, Expressions & Type System

# 1. Python’s Object Model – Everything is an Object

In Python:

* Integers are objects
* Strings are objects
* Functions are objects
* Classes are objects
* Even types themselves are objects

Example:

```python
x = 10
```

Internally:

1. An integer object `10` is created in heap memory.
2. The variable name `x` is stored in the current namespace.
3. `x` references the memory address of that integer object.

Important:
Variables are labels. They are not containers.

---

# 2. Dynamic Typing (What It Really Means)

Python is dynamically typed.

This means:

* Type is attached to the object.
* Variable names are not bound to a fixed type.
* Type checking occurs at runtime.

Example:

```python
x = 10
x = "hello"
```

What happened?

* First, `x` pointed to an int object.
* Then, `x` was reassigned to reference a string object.
* The original integer object may be garbage collected if no references remain.

There is no “type of variable” — only “type of object.”

---

# 3. Type Introspection

Python allows runtime inspection.

```python
x = 10
type(x)
id(x)
```

* `type(x)` returns the object's class.
* `id(x)` returns memory identity (implementation-specific).

This supports Python’s dynamic nature.

---

# 4. Expression Evaluation Model

An expression is any piece of code that produces a value.

Examples:

```python
5 + 3
x * 10
len("hello")
```

Evaluation Process:

1. Operands are evaluated first.
2. Operator is applied.
3. Resulting object is created.

Example:

```python
y = 2 + 3 * 4
```

Steps:

1. 3 * 4 evaluated → 12
2. 2 + 12 evaluated → 14
3. New integer object 14 created.
4. `y` references it.

---

# 5. Operator Precedence (Execution Order)

Python follows strict precedence rules:

1. Parentheses
2. Exponentiation
3. Multiplication / Division
4. Addition / Subtraction
5. Comparisons
6. Logical operators

Always use parentheses for clarity in complex expressions.

---

# 6. Short-Circuit Evaluation

Logical operators use short-circuit logic.

Example:

```python
False and (10 / 0)
```

Python does NOT evaluate `10 / 0`.
Why?
Because in `A and B`, if A is False, result is already determined.

Similarly:

```python
True or (10 / 0)
```

Second expression skipped.

This behavior prevents unnecessary computation and runtime errors.

---

# 7. Truthiness Rules

In Python, every object has a truth value.

Falsy values:

* 0
* 0.0
* ""
* []
* {}
* set()
* None
* False

Everything else is Truthy.

Example:

```python
if []:
    print("True")
```

This will NOT execute.

Internally, Python calls:

* `__bool__()`
* or `__len__()`

If length is zero → False.

---

# 8. Logical Precision (Common Mistakes)

Incorrect:

```python
if x == 5 or 10:
```

This always evaluates to True.

Why?

Expression becomes:

```python
(x == 5) or (10)
```

Since 10 is truthy → whole condition is True.

Correct:

```python
if x == 5 or x == 10:
```

Or better:

```python
if x in (5, 10):
```

---

# 9. Implicit vs Explicit Type Conversion

Implicit conversion is minimal in Python.

Example:

```python
5 + 3.0
```

Integer automatically promoted to float.

But this fails:

```python
"5" + 3
```

Python does NOT guess.
You must explicitly convert:

```python
int("5") + 3
```

---

# 10. Augmented Assignment Behavior

Example:

```python
x = 5
x += 3
```

Internally:

1. x evaluated
2. 3 evaluated
3. Addition performed
4. New object created (for immutable types)
5. x updated to reference new object

Important difference for mutable types:

```python
lst = [1,2]
lst += [3]
```

List is modified in-place.
No new list object created.

---

# 11. Comparison Chaining

Python supports chaining.

```python
1 < x < 10
```

Equivalent to:

```python
1 < x and x < 10
```

But evaluated more efficiently.

---

# 12. Walrus Operator (:=)

Introduced in Python 3.8.

Allows assignment inside expression.

```python
if (n := len(data)) > 10:
    print(n)
```

Reduces repeated computation.

---

# 13. Namespaces

Variables exist inside namespaces.

Types of namespaces:

* Local
* Global
* Built-in

Resolution follows LEGB rule:

Local → Enclosing → Global → Built-in

---

# 14. Memory Implications of Reassignment

Example:

```python
x = [1,2]
y = x
x = [3,4]
```

`y` still points to original list.
Reassignment does NOT modify original object.
It changes reference binding.

Understanding this prevents major logical bugs.

---

# Summary

* Variables are references to objects.
* Type belongs to object, not variable.
* Expressions create new objects (for immutable types).
* Logical operators short-circuit.
* Truthiness is determined via special methods.
* Explicit conversion is required between incompatible types.
* Namespaces control variable resolution.

This understanding is critical before moving into control flow and function mechanics.
