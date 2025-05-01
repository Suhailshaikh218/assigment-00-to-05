"""
This program takes a list of numbers and doubles each element in the list.
It demonstrates how to manipulate elements of a list using indexing.
"""

def main():
    # Original list of numbers
    numbers: list[int] = [1, 2, 3, 4]

    # Loop through the list and double each element
    for i in range(len(numbers)):
        original = numbers[i]
        numbers[i] = original * 2  # Multiply each element by 2

    # Display the result
    print("Doubled list:", numbers)


# This provided line is required to run the main function when executed
if __name__ == '__main__':
    main()
