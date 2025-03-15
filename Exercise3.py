def main():
    # Collecting input from the user
    name = input("Please enter your full name: ")
    hometown = input("Please enter your hometown: ")

    # ensuring the age is an integer, using loop to handle invalid input.
    while True:
        try:
            age = int(input("Please enter your age: "))
            break  # Exit the loop if the age is valid 
        except ValueError: # print error if invalid entered for age
            print("Invalid input for age! Please enter a valid number for your age.")

    # Storing the information in a dictionary
    user_info = {
        'name': name,
        'hometown': hometown,
        'age': age
    }

    # Print the values on separate lines
    print("\nUser Information:")
    print(f"Name: {user_info['name']}")
    print(f"Hometown: {user_info['hometown']}")
    print(f"Age: {user_info['age']}")

if __name__ == "__main__": # run the main function if the script is run directly
    main()
