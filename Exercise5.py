# Dictionary mapping month numbers to days (default for non-leap year)
month_days = {
    1: 31,
    2: 28,  # Will adjust for leap year if needed
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user for a month number
try:
    month = int(input("Enter the month number (1-12): "))

    if 1 <= month <= 12:
        # Check for February and ask about leap year
        if month == 2:
            leap_input = input("Is it a leap year? (yes/no): ").strip().lower()
            if leap_input in ['yes', 'y']:
                print("February has 29 days in a leap year.")
            else:
                print("February has 28 days.")
        else:
            print(f"The month has {month_days[month]} days.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter a number.")
