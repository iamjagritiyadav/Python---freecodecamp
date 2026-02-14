
# Loops & Iteration Patterns

Loops are not just repetition tools.
They are controlled state machines that repeatedly evaluate conditions and update execution state.

In this document we will deeply analyze:

* How loops execute internally
* The iterator protocol
* while vs for at execution level
* range() internals
* Loop control mechanics (break / continue)
* Core loop patterns used in real systems
* Performance implications

---

# 1. What Is Iteration?

Iteration means repeating execution of a block of code until a condition changes.

At CPU level, loops are just:

1. Evaluate condition
2. Jump if true
3. Execute block
4. Jump back

Python abstracts this with `while` and `for`.

---

# 2. The while Loop – Condition-Controlled Execution

Example:

```python
i = 0
while i < 5:
    i += 1
```

Execution flow:

1. Evaluate condition `i < 5`
2. If True → execute block
3. Modify state (`i += 1`)
4. Re-check condition
5. Exit when False

Important:
If state never changes → infinite loop.

---

## 2.1 Infinite Loops

```python
while True:
    pass
```

Used intentionally in:

* Servers
* Event listeners
* Background workers

Exit controlled by `break`.

---

# 3. Loop Control Statements

## break

Immediately exits nearest loop.

## continue

Skips current iteration and jumps to condition check.

Execution detail:

`continue` does NOT restart program — only current loop cycle.

---

# 4. The for Loop – Iterator-Based Execution

Many people misunderstand `for`.

It is NOT index-based by default.
It is iterator-based.

Example:

```python
for x in [1,2,3]:
    print(x)
```

Internally:

1. Python calls `iter()` on the object.
2. Retrieves iterator object.
3. Repeatedly calls `next()`.
4. Stops when StopIteration exception raised.

So `for` is syntactic sugar over iterator protocol.

---

# 5. The Iterator Protocol

An object is iterable if it defines:

* `__iter__()`
* `__next__()`

Manual equivalent of for loop:

```python
it = iter([1,2,3])
while True:
    try:
        value = next(it)
        print(value)
    except StopIteration:
        break
```

This is what `for` does automatically.

---

# 6. range() Internals

`range()` does NOT create a list.

It creates a range object.

Example:

```python
r = range(5)
```

Memory efficient because:

* Stores start, stop, step
* Generates numbers lazily

Time complexity:

* O(1) memory
* O(1) index access

---

# 7. Loop Patterns (Core Engineering Patterns)

---

## 7.1 Accumulator Pattern

Used to build a result over time.

```python
total = 0
for num in numbers:
    total += num
```

State updated every iteration.

Used in:

* Summation
* Counting
* Aggregation

---

## 7.2 Counting Pattern

```python
count = 0
for item in data:
    if condition:
        count += 1
```

Common in analytics.

---

## 7.3 Sentinel Pattern

Used with unknown length input.

```python
while True:
    data = input()
    if data == 'done':
        break
```

Sentinel value terminates loop.

---

## 7.4 Search Pattern

```python
found = False
for item in data:
    if item == target:
        found = True
        break
```

Stops early when match found.

---

## 7.5 Maximum / Minimum Pattern

```python
largest = None
for num in numbers:
    if largest is None or num > largest:
        largest = num
```

Requires careful initialization.

---

# 8. Nested Loops

Example:

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

Time complexity multiplies.

If outer loop runs n times and inner runs m times:
Total operations = n × m

Common in:

* Matrix operations
* Grid traversal

---

# 9. Loop Performance Thinking

Bad pattern:

```python
for i in range(len(lst)):
    if lst[i] in another_list:
```

If `another_list` is large → slow.
Better:
Convert to set for O(1) membership.

---

# 10. Loop and Memory Behavior

In for loops:

Loop variable is reassigned each iteration.

Example:

```python
for x in [1,2,3]:
    pass
```

After loop ends:
`x` still exists in scope (in Python).

---

# 11. Enumerate and Zip

## enumerate

Provides index + value.

```python
for i, val in enumerate(data):
```

Cleaner than range(len()).

---

## zip

Iterates multiple iterables in parallel.

```python
for a, b in zip(list1, list2):
```

Stops at shortest iterable.

---

# 12. Loop vs Comprehension

List comprehension:

```python
[x*x for x in range(5)]
```

More concise.
Often slightly faster.

But avoid over-complicated comprehensions.

---

# 13. Generator-Based Iteration

Instead of building list:

```python
(x*x for x in range(10))
```

Creates generator.
Memory efficient.

---

# 14. Common Loop Mistakes

* Modifying list while iterating over it
* Infinite loop due to missing state change
* Off-by-one errors
* Wrong indentation causing logic bug

---

# Summary

* while is condition-driven
* for is iterator-driven
* range() is lazy and memory efficient
* break and continue alter flow
* Iteration follows iterator protocol
* Nested loops increase time complexity multiplicatively
* Loop patterns are reusable building blocks

Loops are not just repetition.
They are controlled state transitions over time.
Understanding them deeply improves algorithm design.
