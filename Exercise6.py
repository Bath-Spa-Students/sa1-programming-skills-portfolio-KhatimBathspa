# Define the correct password
correct_password = "12345"

# Maximum number of attempts
max_attempts = 5
attempts = 0

# Loop until the correct password is entered or attempts run out
while attempts < max_attempts:
    user_input = input("Enter the password: ")

    if user_input == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) left.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")
