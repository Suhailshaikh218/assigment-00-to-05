"""
Program: pythagorean_theorem_calculator
---------------------------------------
This program calculates the length of the hypotenuse (BC) of a right triangle
using the Pythagorean theorem. It asks for the lengths of the two perpendicular
sides (AB and AC) and outputs the length of the hypotenuse (BC).

The Pythagorean theorem states:
    a^2 + b^2 = c^2
Where:
    - a and b are the two perpendicular sides
    - c is the hypotenuse (BC)
"""

import math  # Import the math library to use the sqrt function

def calculate_hypotenuse(ab, ac):
    """Calculates the hypotenuse using the Pythagorean theorem."""
    return math.sqrt(ab**2 + ac**2)

def main():
    print("Welcome to the Pythagorean Theorem Calculator!")
    print("This program calculates the hypotenuse of a right triangle given the lengths of the other two sides.\n")

    while True:
        try:
            # Get the lengths of the two perpendicular sides from the user
            ab = float(input("Enter the length of AB (one side): "))
            ac = float(input("Enter the length of AC (second side): "))

            # Check if the lengths are positive
            if ab <= 0 or ac <= 0:
                print("❗ Side lengths must be positive numbers. Please try again.\n")
                continue

            # Calculate the hypotenuse using the Pythagorean theorem
            bc = calculate_hypotenuse(ab, ac)

            # Output the result, formatted to 2 decimal places
            print(f"\nThe length of BC (the hypotenuse) is: {bc:.2f}\n")

        except ValueError:
            print("❗ Invalid input. Please enter valid numerical values.\n")

        # Ask the user if they want to perform another calculation
        repeat = input("Do you want to calculate another hypotenuse? (yes/no): ").strip().lower()
        if repeat not in ['yes', 'y']:
            print("\nThank you for using the Pythagorean Theorem Calculator. Goodbye!")
            break

# Run the main function when the script is executed
if __name__ == '__main__':
    main()




