# Control Flow & Functions

This section explores how Python controls execution flow and how functions actually work internally.

We will analyze:

* Conditional logic precision
* Function execution mechanics
* Call stack behavior
* Scope resolution
* Parameter passing model

This is where programming moves from syntax to execution reasoning.

---

# 1. Control Flow – How Execution Is Directed

By default, Python executes statements sequentially (top to bottom).

Control flow statements change that order.

Main control tools:

* if / elif / else
* return
* function calls
* exceptions

---

# 2. Conditional Logic – Beyond Basic if Statements

## 2.1 Boolean Evaluation Model

When Python evaluates:

```python
if condition:
```

It performs:

1. Evaluate expression
2. Convert result to boolean using truthiness rules
3. Execute block if True

This is not limited to `True` or `False`.

Example:

```python
if [1,2,3]:
```

List is truthy → block executes.

---

## 2.2 Logical Operators (and, or, not)

Important behavior:

`and` and `or` return actual operand values — not strictly True/False.

Example:

```python
5 and 10   # returns 10
0 and 10   # returns 0
5 or 10    # returns 5
```

Why?

* `and` returns first falsy or last truthy value
* `or` returns first truthy value

This is used in idiomatic Python.

---

## 2.3 Chained Comparisons

```python
1 < x < 10
```

Internally equivalent to:

```python
(1 < x) and (x < 10)
```

But `x` evaluated only once.

---

## 2.4 Defensive Conditions

Good practice:

```python
if data is not None and len(data) > 0:
```

Short-circuit ensures safe evaluation.

---

# 3. Function Mechanics – What Happens During a Call?

Consider:

```python
def add(a, b):
    return a + b

result = add(2, 3)
```

Internal steps:

1. Function object `add` created in memory.
2. When called, a new stack frame is created.
3. Parameters `a` and `b` are bound to objects 2 and 3.
4. Expression `a + b` evaluated.
5. New integer object 5 created.
6. `return` sends object reference back to caller.
7. Stack frame destroyed.

---

# 4. Call Stack

The call stack tracks active function calls.

Example:

```python
def A():
    B()

def B():
    C()

def C():
    print("Done")
```

Call sequence:

main → A → B → C

Stack grows downward:

| C |
| B |
| A |
| main |

When C finishes → removed
Then B → removed
Then A → removed

This is LIFO (Last In, First Out).

---

# 5. Stack Frame Contents

Each stack frame contains:

* Local variables
* Function arguments
* Instruction pointer
* Return address

When function exits, frame memory is released.

---

# 6. Scope – Where Variables Are Visible

Python follows LEGB rule:

* Local
* Enclosing
* Global
* Built-in

Example:

```python
x = 10

def func():
    print(x)
```

Python searches in:

1. Local scope of func
2. Global scope

Finds x in global.

---

# 7. Local vs Global Variables

If you assign inside function:

```python
def func():
    x = 5
```

Python treats `x` as local.

To modify global:

```python
def func():
    global x
    x = 5
```

Avoid excessive global usage.

---

# 8. Enclosing Scope (Closures Introduction)

Example:

```python
def outer():
    x = 10
    def inner():
        print(x)
    return inner
```

`inner` remembers `x` from outer.

This is closure behavior.

---

# 9. Parameter Passing Model

Python uses:

Call by Object Reference (also called call by sharing).

Meaning:

* Function receives reference to object.
* It cannot rebind caller variable.
* But it can mutate mutable objects.

Example:

```python
def modify(lst):
    lst.append(4)

nums = [1,2,3]
modify(nums)
```

Original list modified.

But:

```python
def reassign(lst):
    lst = [9,9]
```

This does NOT affect original list.

Because only local binding changed.

---

# 10. Mutable Default Argument Trap

Bad practice:

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst
```

Default list created once at function definition.

Correct pattern:

```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

# 11. Return Behavior

If no return statement:

Function returns `None` automatically.

Explicit return ends function immediately.

---

# 12. Recursion and Stack Growth

Each recursive call creates new stack frame.

Too many calls → RecursionError.

Python does not optimize tail recursion.

---

# 13. First-Class Functions

Functions can be:

* Assigned to variables
* Passed as arguments
* Returned from functions

Example:

```python
def greet():
    print("Hi")

x = greet
x()
```

Function object referenced by `x`.

---

# Summary

* Control flow determines execution path.
* Logical operators short-circuit.
* Each function call creates a stack frame.
* Call stack is LIFO.
* Scope follows LEGB rule.
* Parameters are passed by object reference.
* Mutable defaults can cause hidden bugs.

Understanding this prevents subtle logical errors in larger systems.
