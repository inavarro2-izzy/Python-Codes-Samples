# Israel Navarro
# November 8, 2026
# Problem 2: Check if a number is in range(1, 10).

def checkRange(number):
    if number in range(1, 10):
        print(number, "is in the range.")
    else:
        print(number, "is not in the range.")

checkRange(5)
checkRange(10)
