# Error Handling & External Interaction

# Exceptions and Errors

## What is an Exception?

An exception is a runtime error that disrupts normal program execution.

Example:

```python
10 / 0
```

Raises → ZeroDivisionError

If not handled, program crashes.

---

## Built-in Exception Types

Common ones:

* ValueError
* TypeError
* IndexError
* KeyError
* FileNotFoundError
* ZeroDivisionError

Understanding which exception is raised helps in writing precise handlers.

---

## try / except

Basic Structure:

```python
try:
    risky_code()
except ValueError:
    print("Invalid value")
```

Flow:

1. Try block executes.
2. If error occurs → jumps to matching except.
3. Remaining try code is skipped.

---

## Multiple Exceptions

```python
try:
    x = int(input())
except (ValueError, TypeError):
    print("Invalid input")
```

---

## except as e

```python
try:
    1/0
except ZeroDivisionError as e:
    print(e)
```

Stores exception object in variable.

---

## else Block

Executes only if no exception occurs.

```python
try:
    x = 10/2
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
```

---

## finally Block

Always executes.
Used for cleanup (closing files, releasing resources).

```python
try:
    file = open("data.txt")
finally:
    file.close()
```

---

## Raising Exceptions

```python
raise ValueError("Invalid age")
```

Used for manual validation.

---

## Custom Exceptions

```python
class InvalidAgeError(Exception):
    pass

raise InvalidAgeError("Age must be positive")
```

Why?

* Better readability
* Domain-specific errors
* Cleaner architecture

---

# Logging Module

Printing is not logging.
Logging is structured event recording.

---

## Basic Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Application started")
```

---

## Log Levels

* DEBUG → Detailed diagnostic info
* INFO → General events
* WARNING → Something unexpected
* ERROR → Serious issue
* CRITICAL → System failure

Log levels allow filtering.

---

## Custom Format

```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

Useful fields:

* asctime
* levelname
* filename
* lineno

---

## Logging to File

```python
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR
)
```

Important in production systems.

---

# JSON Handling

JSON = JavaScript Object Notation
Used for data exchange (APIs, config files).

---

## Converting Python → JSON

```python
import json

data = {"name": "Jagriti", "age": 21}
json_string = json.dumps(data)
```

---

## Writing JSON to File

```python
with open("data.json", "w") as f:
    json.dump(data, f)
```

---

## Reading JSON

```python
with open("data.json") as f:
    data = json.load(f)
```

---

## JSON Limitations

Cannot serialize:

* Sets
* Custom objects
* Functions

---

## Custom Encoder

```python
class User:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}

json.dumps(user.to_dict())
```

---

# Random Numbers

Python provides multiple randomness sources.
Choosing wrong one is dangerous in security systems.

---

## random Module

```python
import random

random.randint(1,10)
random.random()
random.choice([1,2,3])
```

Pseudo-random generator.
Seed-based.

```python
random.seed(42)
```

Deterministic output for testing.

---

## secrets Module

Used for security-sensitive randomness.

```python
import secrets

secrets.token_hex(16)
```

Cryptographically secure.
Use for:

* Password reset tokens
* API keys

---

## NumPy Random (High Performance)

```python
import numpy as np

np.random.rand(3)
```

Faster for large-scale simulations.

---

# Summary

Exceptions → Prevent crashes and handle failures cleanly
Logging → Structured monitoring system
JSON → Data serialization for APIs and storage
Random vs secrets → Choose based on security needs

This is the foundation of writing production-grade Python code.
