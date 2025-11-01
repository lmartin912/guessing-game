import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} tries!")
            break

guessing_game()
