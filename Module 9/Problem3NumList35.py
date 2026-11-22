# Israel Navarro
# November 19, 2026
# Problem 3: Keep asking for numbers, storing them in a list,
# until the sum of the list is greater than 100.

numbers = []
total = 0

while total <= 100:
    try:
        number = float(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    numbers.append(number)  # Store each entered number.
    total = sum(numbers)     # Recalculate the sum of the list.

print("Numbers entered:", numbers)
print("Total:", total)
