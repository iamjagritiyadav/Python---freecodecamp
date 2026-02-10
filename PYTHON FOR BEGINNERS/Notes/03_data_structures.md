# Python Data Structures

## 1. Why Data Structures Matter

Data structures decide:

* **Time complexity** (how fast your code runs)
* **Space complexity** (how much memory it uses)
* **Scalability** (works for 10 inputs vs 10 million)

**Interview reality:**

> Interviewers don’t care if your code runs — they care **how well** it runs.

---

## 2. Lists

Lists are **ordered, mutable, and allow duplicate elements**.

```python
arr = [1, 2, 3, 4]
```

### Internal Working (Important)

* Implemented as **dynamic arrays**
* Contiguous memory allocation
* Resize happens automatically (amortized cost)

---

### Common Operations

| Operation | Syntax            | Time Complexity |
| --------- | ----------------- | --------------- |
| Access    | `arr[i]`          | O(1)            |
| Append    | `arr.append(x)`   | O(1)*           |
| Insert    | `arr.insert(i,x)` | O(n)            |
| Delete    | `arr.pop(i)`      | O(n)            |
| Search    | `x in arr`        | O(n)            |

`*` amortized O(1)

---

### List Methods (Interview-Focused)

```python
arr.append(5)
arr.extend([6, 7])
arr.insert(1, 100)
arr.remove(3)
arr.pop()
arr.reverse()
arr.count(2)
arr.index(4)
```

---

### Shallow vs Deep Copy (VERY IMPORTANT)

```python
a = [[1,2], [3,4]]
b = a.copy()
b[0][0] = 99
```

* `copy()` → shallow copy
* Nested objects still share reference

**Deep Copy:**

```python
import copy
b = copy.deepcopy(a)
```

---

### When to Use Lists

* Ordered data
* Frequent access by index
* Dynamic size required

---

## 3. Sorting Lists

### In-place Sorting

```python
arr.sort()
```

* Modifies original list
* Returns `None`

### Using `sorted()`

```python
new_arr = sorted(arr)
```

* Returns new list

### Custom Sorting

```python
arr.sort(key=len)
```

**Interview Note:**

> Python uses **Timsort** (hybrid of merge + insertion sort)

Time Complexity: **O(n log n)**

---

## 4. Tuples

Tuples are **ordered, immutable collections**.

```python
t = (1, 2, 3)
```

### Why Tuples Exist

* Faster than lists
* Hashable → usable as dict keys
* Data safety (cannot be modified)

---

### Tuple Packing & Unpacking

```python
a, b = (1, 2)
```

```python
a, *b = (1,2,3,4)
```

---

### List vs Tuple (Interview Table)

| Feature  | List   | Tuple  |
| -------- | ------ | ------ |
| Mutable  | Yes    | No     |
| Speed    | Slower | Faster |
| Hashable | No     | Yes    |

---

## 5. Dictionaries

Dictionaries store **key-value pairs** using **hash tables**.

```python
d = {"a": 1, "b": 2}
```

### Internal Working (VERY IMPORTANT)

* Uses hashing
* Keys must be **immutable & hashable**
* Average lookup: **O(1)**

---

### Dictionary Operations

| Operation | Time |
| --------- | ---- |
| Insert    | O(1) |
| Access    | O(1) |
| Delete    | O(1) |
| Search    | O(1) |

Worst-case: O(n) (hash collision)

---

### Common Methods

```python
d.keys()
d.values()
d.items()
d.get("a", 0)
d.pop("b")
d.update({"c":3})
```

---

### Dictionary Use-Cases

* Frequency counting
* Caching
* Fast lookup tables

---

## 6. Sets

Sets are **unordered, mutable collections of unique elements**.

```python
s = {1, 2, 3}
```

### Internal Working

* Implemented using hash tables
* No duplicates allowed

---

### Set Operations

```python
s.add(4)
s.remove(2)
s.union({5,6})
s.intersection({1,2})
s.difference({3})
```

---

### Time Complexity

| Operation  | Time |
| ---------- | ---- |
| Add        | O(1) |
| Remove     | O(1) |
| Membership | O(1) |

---

### Set vs List (Interview)

| Feature    | List | Set  |
| ---------- | ---- | ---- |
| Order      | Yes  | No   |
| Duplicates | Yes  | No   |
| Search     | O(n) | O(1) |

---

## 7. List Comprehension

Concise way to create lists.

```python
squares = [x*x for x in range(5)]
```

### With Condition

```python
evens = [x for x in range(10) if x % 2 == 0]
```

### Nested Comprehension

```python
matrix = [[i*j for j in range(3)] for i in range(3)]
```

**Interview Warning:**

> Avoid complex nested comprehensions — readability matters.

---

## 8. Mutability Explained (VERY IMPORTANT)

| Type  | Mutable |
| ----- | ------- |
| list  | Yes     |
| dict  | Yes     |
| set   | Yes     |
| tuple | No      |
| str   | No      |

**Interview Trap:**

> Mutable objects passed to functions can be modified unintentionally.

---

## 9. Common Interview Traps

❌ Using list when set is better

❌ Modifying list while iterating

❌ Assuming dicts are unordered (Python 3.7+ preserves insertion order)

❌ Forgetting shallow copy behavior

---

## 10. Rapid-Fire Interview Questions

1. Why dictionary lookup is O(1)?
2. Why tuples are faster than lists?
3. Difference between set and dict?
4. When list comprehension is bad?
5. Why mutable default arguments are dangerous?

---

## 11. Answers to Interview Questions

### 1. Why dictionary lookup is O(1)?

Because dictionaries use hash tables, allowing direct index access via hash values.

---

### 2. Why tuples are faster than lists?

Because tuples are immutable, Python can optimize memory and access speed.

---

### 3. Difference between set and dict?

* Set stores only keys
* Dict stores key-value pairs

---

### 4. When list comprehension is bad?

When logic becomes complex or readability is reduced.

---

### 5. Why mutable default arguments are dangerous?

Because default arguments are evaluated once and shared across function calls.

```python
def f(x, arr=[]):
    arr.append(x)
    return arr
```



Next: `04_functions_and_oop.md`
