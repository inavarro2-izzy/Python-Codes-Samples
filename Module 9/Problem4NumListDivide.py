# Israel Navarro
# November 19, 2026
# Problem 4: Use a while loop with a counter from 0 through 49.
# Add counter values divisible by 10 to a list named tens.

tens = []
counter = 0

while counter < 50:
    if counter % 10 == 0:  # A remainder of zero means divisible by 10.
        tens.append(counter)
    counter += 1

print("Numbers divisible by 10:", tens)
