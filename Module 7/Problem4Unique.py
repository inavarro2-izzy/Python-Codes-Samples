# Israel Navarro
# November 8, 2026
# Problem 4: Return unique numbers using append().

def uniqueNumbers(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique

numbers = [1, 3, 3, 3, 6, 2, 3, 5]
print("Original list:", numbers)
print("Unique list:", uniqueNumbers(numbers))
