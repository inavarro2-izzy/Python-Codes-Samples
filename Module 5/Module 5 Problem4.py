
# Name: Israel Navarro
# Date: October 25, 2026
# Description: This program uses a loop to check
# numbers from 1 to 50. It prints a message if
# a number is divisible by 3, 5, or both.

# Loop through numbers from 1 to 50
for number in range(1, 51):

    # Check if divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both")

    # Check if divisible by 3
    elif number % 3 == 0:
        print("Divisible by three")

    # Check if divisible by 5
    elif number % 5 == 0:
        print("Divisible by five")

    # Print the number if not divisible by either
    else:
        print(number)
