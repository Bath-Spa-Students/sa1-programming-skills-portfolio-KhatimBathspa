# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function
def main():
    try:
        num = int(input("Enter a number: "))
        result = check_even_odd(num)
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
