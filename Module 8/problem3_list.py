# Israel Navarro
# November 14, 2026
# Check whether the number 5 appears in a list.

def check_for_five(numbers):
    if 5 in numbers:
        print("The value 5 is in the list.")
    else:
        print("The value 5 is not in the list.")


if __name__ == "__main__":
    check_for_five([1, 2, 5, 7, 9])
    check_for_five([1, 2, 3, 7, 9])
