import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    wins = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    if wins[user] == computer:
        return "user"
    else:
        return "computer"

def play_game():
    print("Rock - Paper - Scissors Game")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.\n")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        if user_choice == 'quit':
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        again = input("\nPlay again? (yes/no): ").lower()
        if again != 'yes':
            break
        print()

    print(f"\nFinal Score -> You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
