# Israel Navarro
# November 1, 2026
# Problem 6: Calculate a factorial with a for loop and with math.factorial.
import math

number = int(input("Enter a nonnegative whole number: "))
if number < 0:
    print("Factorials are not defined for negative integers.")
else:
    result = 1
    for value in range(1, number + 1):
        result *= value
    print("Calculated factorial:", result)
    print("math.factorial result:", math.factorial(number))
