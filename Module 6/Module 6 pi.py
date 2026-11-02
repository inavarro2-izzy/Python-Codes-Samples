# Israel Navarro
# November 1, 2026
# Problem 4: Approximate pi and compare the result with math.pi.
# The Nilakantha series starts with 3 and adds alternating fractions.
import math

approximation = 3.0
for n in range(2, 2002, 4):
    approximation += 4 / (n * (n + 1) * (n + 2))
    approximation -= 4 / ((n + 2) * (n + 3) * (n + 4))

print("Approximation of pi:", approximation)
print("Value of math.pi:", math.pi)
