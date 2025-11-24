import random
import time

# -----------------------------------------
# Simple Number Guessing Adventure (60+ lines)
# -----------------------------------------

def slow_print(text, delay=0.03):
    """Print text slowly to make it feel like an adventure."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    slow_print("Welcome, traveler!")
    slow_print("You have entered the Cave of Numbers.")
    slow_print("To escape, you must guess the secret number.")
    slow_print("---------------------------------------------")
    print()

def get_difficulty():
    """Let the player choose difficulty level."""
    slow_print("Choose your difficulty:")
    slow_print("1. Easy (1–10)")
    slow_print("2. Medium (1–50)")
    slow_print("3. Hard (1–100)")
    
    while True:
        choice = input("Enter difficulty (1/2/3): ")
        if choice == "1":
            return 10
        elif choice == "2":
            return 50
        elif choice == "3":
            return 100
        else:
            print("Invalid choice. Try again.")

def play_game(limit):
    """Main game logic."""
    secret = random.randint(1, limit)
    attempts = 0

    slow_print(f"\nA number between 1 and {limit} has been chosen...")
    slow_print("Try to guess it!\n")

    while True:
        guess = input("Your guess: ")

        if not guess.isdigit():
            print("Numbers only! Try again.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            slow_print("\nYou got it!")
            slow_print(f"The secret number was {secret}.")
            slow_print(f"You escaped the cave in {attempts} attempts!")
            break

def play_again():
    """Ask if the player wants to play again."""
    choice = input("\nPlay again? (y/n): ").lower()
    return choice == "y"

def main():
    intro()
    while True:
        limit = get_difficulty()
        play_game(limit)
        if not play_again():
            slow_print("\nFarewell, brave traveler!")
            break

# Run the game
if __name__ == "__main__":
    main()
