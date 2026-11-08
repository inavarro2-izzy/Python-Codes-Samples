# Israel Navarro
# November 8, 2026
# Problem 3: Multiply all the numbers in a list.

def multiplyList(numbers):
    result = 1
    for number in numbers:
        result = result * number
    return result

numbers = [5, 2, 7, -1]
print("List:", numbers)
print("Product:", multiplyList(numbers))
