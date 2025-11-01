import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\nWelcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100:")

    while True:
        guess = int(input("> "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts!")
            break
    
    return attempts

# Main game loop (play again feature)
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again not in ("yes", "y"):
        print("Thanks for playing! 👋")
        break
