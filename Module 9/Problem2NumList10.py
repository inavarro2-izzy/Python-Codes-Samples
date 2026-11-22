# Israel Navarro
# November 19, 2026
# Problem 2: Use a while loop to build list L with numbers from 0 to 10.

L = []
counter = 0

while counter <= 10:
    L.append(counter)  # Add the current number to the list.
    counter += 1       # Move to the next number.

print("List L:", L)
