# Operators and Control Flow

## 1. Operators in Python

Operators are used to perform operations on variables and values.

---

## 2. Arithmetic Operators

Used for mathematical operations.

| Operator | Description    | Example  |
| -------- | -------------- | -------- |
| `+`      | Addition       | `3 + 2`  |
| `-`      | Subtraction    | `5 - 2`  |
| `*`      | Multiplication | `4 * 2`  |
| `/`      | Division       | `5 / 2`  |
| `//`     | Floor Division | `5 // 2` |
| `%`      | Modulus        | `5 % 2`  |
| `**`     | Exponentiation | `2 ** 3` |

```python
print(5 / 2)   # 2.5
print(5 // 2)  # 2
```

**Interview Tip:**

> `/` always returns float, even if divisible.

---

## 3. Comparison Operators

Used to compare values and return boolean results.

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | Equal to         |
| `!=`     | Not equal        |
| `>`      | Greater than     |
| `<`      | Less than        |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

```python
print(10 > 5)   # True
print(3 == 4)   # False
```

---

## 4. Boolean Operators

Used to combine conditional statements.

| Operator | Description       |
| -------- | ----------------- |
| `and`    | True if both true |
| `or`     | True if any true  |
| `not`    | Negates condition |

```python
print(True and False)  # False
print(True or False)   # True
```

**Short-circuiting:**

* Python stops evaluation early if result is known.

---

## 5. Bitwise Operators

Operate on bits (binary level).

| Operator | Meaning     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left shift  |    |
| `>>`     | Right shift |    |

```python
print(5 & 3)  # 1
```

**Interview Note:**

* Common in low-level and optimization problems.

---

## 6. `is` and `in` Operators

### `is`

Checks **object identity**, not value.

```python
a = None
print(a is None)
```

### `in`

Checks membership.

```python
print('a' in 'cat')
```

---

## 7. Ternary Operator

Single-line conditional expression.

```python
result = "Pass" if marks >= 40 else "Fail"
```

**Interview Tip:**

> Avoid overusing ternary — readability matters.

---

## 8. Control Statements

Used to control the flow of execution.

---

## 9. if, elif, else

```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

---

## 10. Loops

### for Loop

```python
for i in range(5):
    print(i)
```

### while Loop

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## 11. break and continue

```python
for i in range(5):
    if i == 3:
        break
```

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

---

## 12. Common Mistakes

❌ Using `is` instead of `==`

❌ Infinite loops due to missing condition update

❌ Confusing bitwise `&` with logical `and`

---

## 13. Interview Questions

1. Difference between `and` and `&`?
2. What is short-circuit evaluation?
3. Difference between `break` and `continue`?
4. When to use ternary operator?
5. Why is `is` preferred for None comparison?

---

## 14. Answers to Interview Questions

### 1. Difference between `and` and `&`

* `and` → logical operator
* `&` → bitwise operator

```python
True and False   # False
5 & 3            # 1
```

---

### 2. What is short-circuit evaluation?

Python stops evaluating expressions once the result is determined.

```python
False and print("Hello")  # print never runs
```

---

### 3. Difference between `break` and `continue`

| break      | continue                |
| ---------- | ----------------------- |
| Stops loop | Skips current iteration |

---

### 4. When to use ternary operator?

Use it for **simple conditional assignments**, not complex logic.

---

### 5. Why is `is` preferred for None comparison?

`None` is a singleton object, so identity comparison is reliable.

```python
if x is None:
    pass
```

---



Next: `03_data_structures.md`
