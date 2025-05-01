"""
This program defines a function that takes a list of numbers
and returns the sum of those numbers. It demonstrates the use
of loops and functions in Python.
"""

def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    
    Args:
        numbers (list[int]): A list of integers to sum.

    Returns:
        int: The total sum of the numbers.
    """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number
    return total_so_far


def main():
    # Define a sample list of numbers to add
    numbers: list[int] = [1, 2, 3, 4, 5]
    
    # Get the sum using our function
    sum_of_numbers: int = add_many_numbers(numbers)

    # Print the result with a helpful message
    print("The sum of", numbers, "is:", sum_of_numbers)


# Required line to call the main function when the script runs
if __name__ == '__main__':
    main()
