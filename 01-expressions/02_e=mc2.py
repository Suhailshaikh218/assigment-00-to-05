"""
Program: einstein_energy_calculator
-----------------------------------
This program calculates the equivalent energy (E) from a given
mass (m) using Einstein's famous equation:

    E = m * c^2

Where:
- E is energy in joules
- m is mass in kilograms (provided by the user)
- c is the speed of light (299,792,458 m/s)

This version allows the user to enter multiple values and
includes input validation for best practice.
"""

# Constant: Speed of light in meters per second
SPEED_OF_LIGHT = 299_792_458  # m/s

def calculate_energy(mass_kg):
    """Returns energy in joules for given mass using E = m * c^2."""
    return mass_kg * (SPEED_OF_LIGHT ** 2)

def main():
    print("Welcome to the Einstein Energy Calculator!")
    print("This program calculates energy from mass using E = m * c^2.")
    print("Enter a mass in kilograms (or type 'q' to quit).\n")

    while True:
        user_input = input("Enter kilos of mass: ")

        if user_input.strip().lower() in ['q', 'quit', 'exit']:
            print("\nThank you for using the calculator. Goodbye!")
            break

        try:
            mass = float(user_input)

            if mass < 0:
                print("❗ Mass cannot be negative. Please enter a positive number.\n")
                continue

            energy = calculate_energy(mass)

            # Output results
            print("\ne = m * C^2...")
            print(f"m = {mass} kg")
            print(f"C = {SPEED_OF_LIGHT} m/s")
            print(f"{energy} joules of energy!\n")

        except ValueError:
            print("❗ Invalid input. Please enter a valid number or 'q' to quit.\n")

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
