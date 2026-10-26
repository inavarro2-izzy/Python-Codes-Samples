# Name: Israel Navarro
# Date: October 24, 2026
# Description: Print each number, then each number with its square.

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Part A: Print each number on a separate line.
print("Part A: Numbers")
for number in numbers:
    print(number)

# Part B: Print each number and its square.
print("\nPart B: Numbers and squares")
for number in numbers:
    print(number, "squared =", number ** 2)
