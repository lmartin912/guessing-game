import random

print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100: ")

    try:
        guess = int(guess)
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! The number was {number}.")
        print(f"You guessed it in {attempts} attempts!")
        break
