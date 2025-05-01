"""
Program: dice_roller_simulation
--------------------------------
This program simulates rolling two dice, prints the result of each die roll, and displays the total sum of both dice.
Each die is assumed to have 6 sides.
"""

import random  # Import the random library to simulate random die rolls

# Constant for the number of sides on each die
NUM_SIDES: int = 6

def roll_dice():
    """
    Simulates rolling two dice and returns the results as a tuple.
    """
    die1: int = random.randint(1, NUM_SIDES)  # Roll the first die
    die2: int = random.randint(1, NUM_SIDES)  # Roll the second die
    return die1, die2  # Return the results as a tuple (die1, die2)

def main():
    # Roll the dice
    die1, die2 = roll_dice()  # Get the results of the dice rolls
    
    # Calculate the total of both dice
    total: int = die1 + die2
    
    # Display the results to the user
    print("Rolling two dice...\n")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")
    
    # Optional: Displaying additional info for educational purposes
    print("\nNote: Each die has", NUM_SIDES, "sides, and each roll is random.")
    print("Enjoy your dice roll simulation!")

# This line calls the main function when the script is run directly
if __name__ == '__main__':
    main()
