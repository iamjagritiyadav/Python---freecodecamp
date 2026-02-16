
# Regular Expressions: Engine & Parsing

Regular expressions (regex) are not magic text tools.
They are pattern-matching engines with specific execution rules, performance characteristics, and limitations.

In this document we explore:

* How the regex engine works internally
* Pattern compilation
* Matching vs extracting
* Greedy vs non-greedy behavior
* Backtracking mechanics
* Performance pitfalls
* Real-world parsing strategy

---

# 1. What Is a Regular Expression?

A regular expression is a pattern description language.

It describes:

* What to match
* How many times
* In what order
* Under what constraints

Example:

```python
import re
re.findall(r"\d+", "Order 123 and 456")
```

Matches one or more digits.

---

# 2. Regex Execution Model

When you use:

```python
re.findall(pattern, text)
```

Internally:

1. Pattern is compiled into a regex object.
2. Engine scans text left to right.
3. Attempts to match pattern at each position.
4. Returns matches depending on method used.

The engine in Python (`re` module) is a **backtracking engine**.

---

# 3. Pattern Compilation

Instead of repeatedly calling:

```python
re.findall(pattern, text)
```

Better approach for repeated usage:

```python
compiled = re.compile(pattern)
compiled.findall(text)
```

Why?

Compilation step:

* Converts pattern string into internal state machine
* Improves performance when reused

---

# 4. Core Pattern Elements

Common tokens:

`.`        → Any character
`\d`       → Digit
`\w`       → Word character
`\s`       → Whitespace
`^`        → Start of string
`$`        → End of string

Quantifiers:

`*`        → 0 or more
`+`        → 1 or more
`?`        → 0 or 1
`{m,n}`    → Range repetition

---

# 5. Matching vs Extracting

Different functions behave differently.

## re.match()

Matches only at beginning of string.

## re.search()

Searches entire string.

## re.findall()

Returns all matching substrings.

## re.finditer()

Returns iterator of match objects.

Use `finditer()` when you need match metadata (positions).

---

# 6. Capturing Groups

Example:

```python
re.findall(r"(\d+)-(\d+)", "10-20")
```

Returns:

```
[("10", "20")]
```

Parentheses create capturing groups.

To avoid capturing:

```python
(?:pattern)
```

Non-capturing group.

---

# 7. Greedy vs Non-Greedy

Default behavior is greedy.

Example:

```python
re.findall(r"<.*>", "<a> <b>")
```

Greedy `.*` matches longest possible string.
Result:

```
['<a> <b>']
```

Non-greedy version:

```python
re.findall(r"<.*?>", "<a> <b>")
```

Now matches shortest pattern.

Result:

```
['<a>', '<b>']
```

`?` after quantifier makes it non-greedy.

---

# 8. Backtracking – The Core Mechanism

Python regex engine uses backtracking.

Process:

1. Try to match pattern greedily.
2. If later part fails → backtrack.
3. Try shorter match.

Example:

Pattern:

```
(a+)+
```

On long string of 'a's → can cause catastrophic backtracking.

This may cause severe performance slowdown.

---

# 9. Catastrophic Backtracking

Occurs when:

* Nested quantifiers exist
* Pattern is ambiguous
* Engine repeatedly tries alternatives

Example dangerous pattern:

```
(.*a)*
```

Avoid ambiguous nested patterns.

---

# 10. Anchors and Boundaries

`^` → Start of string
`$` → End of string
`\b` → Word boundary

Example:

```python
re.findall(r"^Error", text)
```

Matches only lines starting with "Error".

---

# 11. Flags

Common flags:

`re.IGNORECASE`
`re.MULTILINE`
`re.DOTALL`

Example:

```python
re.findall(pattern, text, re.IGNORECASE)
```

Flags modify engine behavior.

---

# 12. When NOT to Use Regex

Do not use regex when:

* Simple split() works
* Fixed-position slicing works
* Structure is simple and consistent

Regex is powerful but harder to maintain.

---

# 13. Real Parsing Strategy

When parsing text, follow structured approach:

1. Understand format
2. Decide parsing strategy

   * split
   * slicing
   * regex
3. Validate structure
4. Extract safely
5. Handle errors gracefully

Example: Extract email addresses

```python
re.findall(r"[\w\.-]+@[\w\.-]+", text)
```

---

# 14. Performance Considerations

* Precompile patterns
* Avoid nested greedy quantifiers
* Use specific patterns instead of `.*`
* Prefer non-greedy where appropriate

---

# 15. Regex in Data Pipelines

Regex commonly used in:

* Log parsing
* Email extraction
* Data cleaning
* URL extraction
* Tokenization

But must be controlled and validated.

---

# 16. Common Mistakes

* Forgetting raw string prefix `r""`
* Using greedy patterns unintentionally
* Not anchoring patterns when needed
* Ignoring performance risks

---

# Summary

* Python uses backtracking regex engine.
* Patterns are compiled to internal state machine.
* Greedy vs non-greedy changes match scope.
* Backtracking can cause performance issues.
* Regex is powerful but should be used deliberately.

Regex is a precision tool — not a blunt instrument.
