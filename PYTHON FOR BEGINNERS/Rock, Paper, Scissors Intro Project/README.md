# Rock–Paper–Scissors

## Concepts Used (with direct code mapping)

---

### 1. Importing Modules

Used to access built-in functionality.

```python
import random
```

Used for:

* `random.choice()` → computer move

---

### 2. Functions

Used to split logic and keep code clean.

```python
def get_choices():
def check_win(player, computer):
```

Why:

* One function → one responsibility
* Easy testing and reuse

---

### 3. User Input

Takes input from terminal.

```python
player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
```

Key points:

* `input()` always returns string
* `.lower()` avoids case mismatch bugs

---

### 4. Lists

Used to store multiple values.

```python
options = ["rock", "paper", "scissors"]
```

Why:

* Valid choices grouped in one variable

---

### 5. Random Selection

Computer choice logic.

```python
computer_choice = random.choice(options)
```

Key idea:

* Picks one element randomly from list

---

### 6. Dictionaries

Used to group related data.

```python
choices = {
    "player": player_choice,
    "computer": computer_choice
}
```

Why:

* Access using keys → `choices["player"]`

---

### 7. Return Statement

Send data back from function.

```python
return choices
```

Used to:

* Pass values from `get_choices()` to main logic

---

### 8. Function Arguments

Passing data into functions.

```python
def check_win(player, computer):
```

Why:

* Function works on dynamic values
* No hard-coding

---

### 9. Conditional Statements

Decision making.

```python
if player == computer:
elif player == "rock":
elif player == "paper":
elif player == "scissors":
```

Used for:

* Game rules
* Win / lose / tie logic

---

### 10. Nested If Statements

Handling sub-conditions.

```python
if computer == "scissors":
    return "You win"
else:
    return "You lose"
```

Why:

* One condition depends on another

---

### 11. String Formatting (f-strings)

Readable output.

```python
print(f"You chose {player}, computer chose {computer}")
```

Why:

* Cleaner than string concatenation

---

### 12. Program Flow

Main execution logic.

```python
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
```

Flow:

1. Take input
2. Generate computer choice
3. Compare
4. Print result

---
