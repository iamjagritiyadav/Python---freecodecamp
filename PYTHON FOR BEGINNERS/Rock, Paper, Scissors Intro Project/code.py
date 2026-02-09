import random

# -----------------------------
# Get choices
# -----------------------------
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {
        "player": player_choice,
        "computer": computer_choice
    }

    return choices


# -----------------------------
# Check winner
# -----------------------------
def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        return "It's a tie!"

    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."

    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cut paper! You lose."

    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

    else:
        return "Invalid input! Please choose rock, paper, or scissors."


# -----------------------------
# Main game
# -----------------------------
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
