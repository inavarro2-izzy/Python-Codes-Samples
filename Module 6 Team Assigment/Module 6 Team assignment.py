
# Israel Navarro
# November 2, 2026
# CSS 225 - Module 6 Team Assignment
# Number Guessing Game
# This program generates a random number and allows
# the user to guess if their number is higher or lower.
# Extra Credit: The user can keep playing until choosing N.

import random

print("Welcome to the Number Guessing Game!")

play_again = "Y"

while play_again == "Y":

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    print("\nI picked a number between 1 and 100.")

    guessed_correctly = False

    while not guessed_correctly:

        # Ask the user to enter a guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        # Check whether the guess is within range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        else:
            # Nested if...else statements
            if guess == secret_number:
                print("Congratulations! You guessed correctly!")
                guessed_correctly = True
            else:
                if guess < secret_number:
                    print("Too low! Try a higher number.")
                else:
                    print("Too high! Try a lower number.")

    # Extra credit: Ask whether to play again
    play_again = input(
        "\nWould you like to guess another number (Y/N)? "
    ).strip().upper()

    while play_again != "Y" and play_again != "N":
        print("Please enter Y or N.")
        play_again = input(
            "Would you like to guess another number (Y/N)? "
        ).strip().upper()

print("\nThank you for playing!")
