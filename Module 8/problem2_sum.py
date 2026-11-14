# Israel Navarro
# November 14, 2026
# Compare the sum of two user-entered numbers with 10.

def compare_sum():
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    total = first + second
    print("Sum:", total)
    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")


if __name__ == "__main__":
    compare_sum()