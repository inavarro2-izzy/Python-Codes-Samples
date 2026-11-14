# Israel Navarro
# November 14, 2026
# Return True for leap years and False for non-leap years.

def is_leap_year(year):
    # Century years must be divisible by 400 to be leap years.
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


if __name__ == "__main__":
    for year in [2024, 2025, 1900, 2000]:
        print(year, "is a leap year:", is_leap_year(year))
