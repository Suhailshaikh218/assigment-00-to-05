"""
Program: triangle_perimeter
---------------------------
This program prompts the user to enter the lengths
of all three sides of a triangle and calculates
the perimeter by summing those lengths.
"""

def main():
    # Prompt for each side length and convert to float
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Display the result
    print(f"The perimeter of the triangle is {perimeter}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

