
import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock-Paper-Scissors Game")
print("Instructions: Type rock, paper, or scissors")

while True:
    user_choice = input("\nYour choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print(f"User chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You Win! 🎉")
        user_score += 1

    else:
        print("Result: You Lose! 😢")
        computer_score += 1

    # Display scores
    print(f"Score ➜ You: {user_score} | Computer: {computer_score}")

    # Play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("\nThanks for playing! 👋")
        break
