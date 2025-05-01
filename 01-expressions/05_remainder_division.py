"""
Program: division_with_remainder
-----------------------------------
This program asks the user for two numbers, then divides the first number by the second
and prints both the quotient and the remainder. It also handles edge cases like division by zero.
"""

def get_valid_integer(prompt):
    """Function to get a valid integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❗ Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the Division with Remainder Program!")
    print("This program divides one number by another and shows both the quotient and remainder.\n")
    
    while True:
        # Get two valid integers from the user
        dividend = get_valid_integer("Please enter an integer to be divided: ")
        divisor = get_valid_integer("Please enter an integer to divide by: ")

        # Check if divisor is zero to avoid division by zero
        if divisor == 0:
            print("❗ Error: Division by zero is not allowed. Please try again.\n")
            continue

        # Perform the division and calculate the quotient and remainder
        quotient = dividend // divisor
        remainder = dividend % divisor
        
        # Display the result
        print(f"\nThe result of {dividend} divided by {divisor} is:")
        print(f"Quotient: {quotient}")
        print(f"Remainder: {remainder}\n")

        # Ask if the user wants to perform another division
        repeat = input("Do you want to perform another division? (yes/no): ").strip().lower()
        if repeat not in ['yes', 'y']:
            print("\nThank you for using the Division with Remainder program. Goodbye!")
            break

# Run the main function when the script is executed
if __name__ == '__main__':
    main()


