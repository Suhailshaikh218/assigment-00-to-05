"""
Program: feet_to_inches_converter
---------------------------------
This program converts feet to inches. It takes the number of feet
as input from the user and performs the conversion using the formula:

    inches = feet * 12

Where:
- 1 foot = 12 inches
"""

# Constant: Conversion factor for feet to inches
FEET_TO_INCHES = 12  # 1 foot = 12 inches

def convert_feet_to_inches(feet):
    """Converts feet to inches."""
    return feet * FEET_TO_INCHES

def main():
    print("Welcome to the Feet-to-Inches Converter!")
    print("This program will convert the number of feet you input into inches.\n")

    while True:
        user_input = input("Enter number of feet (or type 'q' to quit): ")

        if user_input.strip().lower() in ['q', 'quit', 'exit']:
            print("\nThank you for using the converter. Goodbye!")
            break

        try:
            feet = float(user_input)

            if feet < 0:
                print("❗ Number of feet cannot be negative. Please enter a positive number.\n")
                continue

            inches = convert_feet_to_inches(feet)

            # Output the result
            print(f"\n{feet} feet is equal to {inches} inches.\n")

        except ValueError:
            print("❗ Invalid input. Please enter a valid number or 'q' to quit.\n")

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
