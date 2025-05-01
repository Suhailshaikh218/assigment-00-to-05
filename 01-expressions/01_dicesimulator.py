"""
Program: dice_simulator
------------------------
This program rolls two dice three times and displays the result
of each roll. It also demonstrates how variable scope works in Python.
"""

import random

# Total number of faces on a standard die
DIE_SIDES = 6

def roll_two_dice():
    """
    Rolls two dice and prints each die's value and their sum.
    """
    first_die = random.randint(1, DIE_SIDES)
    second_die = random.randint(1, DIE_SIDES)
    total = first_die + second_die
    print(f"First Die: {first_die}, Second Die: {second_die} → Sum: {total}")

def main():
    # Local variable only in main(), not affected by roll_two_dice()
    first_die = 99
    print(f"[main] Initial value of first_die: {first_die}\n")

    print("Rolling two dice three times:\n")
    for i in range(1, 4):
        print(f"Roll {i}: ", end="")
        roll_two_dice()

    print(f"\n[main] Final value of first_die: {first_die}")

# Ensures main() runs when this script is executed directly
if __name__ == '__main__':
    main()

