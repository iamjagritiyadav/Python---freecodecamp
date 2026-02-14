# Execution Model & Programming Foundations

# 1. What Does “Programming” Actually Mean?

Programming is the act of giving a computer a precise, step-by-step set of instructions to solve a problem.

A computer:

* Does not think
* Does not infer
* Does not assume
* Only executes instructions exactly as written

Programming is about translating logic into instructions that a machine can execute deterministically.

---

# 2. Hardware Architecture Basics

To understand Python execution, we must understand basic hardware components.

## CPU (Central Processing Unit)

The CPU executes instructions.

It performs:

* Arithmetic operations
* Logical operations
* Memory addressing
* Control flow decisions

The CPU does NOT understand Python directly.
It understands machine code (binary instructions).

---

## Memory (RAM)

RAM stores:

* Running programs
* Variables
* Temporary data

Important:
RAM is volatile — data disappears when power is off.

---

## Storage (SSD / HDD)

Stores:

* Python interpreter
* Your .py files
* Installed libraries

When you run a program:

1. Code moves from storage → RAM
2. CPU executes instructions from RAM

---

# 3. Interpreter vs Compiler

Python is an interpreted language.

But technically, CPython does BOTH compilation and interpretation.

---

## Step-by-Step Execution Process

When you run:

```bash
python program.py
```

This happens internally:

1. Source code (.py file) is read.
2. Python compiles it into bytecode.
3. Bytecode is executed by the Python Virtual Machine (PVM).

---

## What is Bytecode?

Bytecode is an intermediate representation of your program.

It is:

* Lower-level than Python
* Higher-level than machine code
* Platform-independent

Stored in:

```
__pycache__/
```

Files like:

```
program.cpython-312.pyc
```

---

# 4. Python Virtual Machine (PVM)

The PVM:

* Reads bytecode
* Executes instructions one by one

It acts as a layer between:

Python code → Machine code

This is why Python is portable.

---

# 5. Execution Flow of a Python Program

Consider:

```python
x = 5
y = x + 3
print(y)
```

Internally:

1. Memory space is allocated.
2. Integer object 5 is created.
3. Variable x references that object.
4. Integer object 3 is created.
5. Addition operation executed.
6. New integer object 8 created.
7. Variable y references that object.
8. print() sends value to stdout.

Important:
Variables do NOT store values.
They store references to objects.

---

# 6. Stack vs Heap Memory

## Stack

Stores:

* Function calls
* Local variables
* Execution frames

Each function call creates a stack frame.
When function ends → frame is removed.

---

## Heap

Stores:

* Objects
* Lists
* Dictionaries
* Large data

Managed by Python’s memory manager.

---

# 7. Dynamic Typing

In Python:

```python
x = 10
x = "hello"
```

This works because:

* Variables are just labels
* Objects carry type information

Python is dynamically typed.

Type checking happens at runtime.

---

# 8. Execution is Sequential (Unless Controlled)

Python executes code line-by-line.

Control structures modify flow:

* if
* loops
* functions
* exceptions

But default behavior is sequential execution.

---

# 9. Errors vs Exceptions

## Syntax Error

Detected during compilation to bytecode.
Program never runs.

## Runtime Error (Exception)

Occurs during execution.
Program stops unless handled.

---

# 10. Deterministic Execution

Computers are deterministic.

Given same input and environment:
Output will be same (unless randomness involved).

This predictability is what allows debugging.

---

# 11. Mental Model You Must Build

When writing Python, always think:

* What objects are being created?
* Where are they stored?
* What references point to them?
* What happens when function exits?
* What is happening in memory?

Programming mastery starts when you stop seeing code as text and start seeing it as execution flow.

---

# Summary

* Python source → Bytecode → PVM → CPU
* CPU executes machine instructions
* Variables store references, not values
* Memory split into stack and heap
* Execution is sequential unless controlled
* Python is dynamically typed

Understanding execution model is foundational for everything else in this course.
