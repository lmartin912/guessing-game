import random

print("🎯 Welcome to the Number Guessing Game!")

print("\nSelect Difficulty:")
print("1. Easy (1–50, unlimited guesses)")
print("2. Medium (1–100, 10 guesses)")
print("3. Hard (1–200, 7 guesses)")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    max_num = 50
    attempts = float('inf')
    print("\nEasy Mode selected! ✅")
elif choice == "2":
    max_num = 100
    attempts = 10
    print("\nMedium Mode selected! ⚠️")
elif choice == "3":
    max_num = 200
    attempts = 7
    print("\nHard Mode selected! 💀 Good luck!")
else:
    print("Invalid choice. Defaulting to Medium.")
    max_num = 100
    attempts = 10

secret_number = random.randint(1, max_num)
guess_count = 0

while guess_count < attempts:
    try:
        guess = int(input(f"Guess a number between 1 and {max_num}: "))
    except ValueError:
        print("❌ Invalid input. Enter a number.")
        continue

    guess_count += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed the number in {guess_count} tries!")
        break

# Out of attempts
if guess_count >= attempts and guess != secret_number:
    print(f"😞 You're out of guesses! The number was {secret_number}.")
    
play_again = input("\nPlay again? (y/n): ").lower()
if play_again == "y":
    exec(open(__file__).read())  # restart program
else:
    print("Thanks for playing! 👋")
