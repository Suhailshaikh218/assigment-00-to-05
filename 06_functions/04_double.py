def double(num: int):
    """
    Returns the result of multiplying num by 2.
    """
    return num * 2

def main():
    """
    Prompts the user for a number, doubles it, and prints the result.
    """
    num = int(input("Enter a number: "))  # Prompt user for input and convert it to an integer
    num_times_2 = double(num)  # Call double() function with user input
    print("Double that is", num_times_2)  # Output the result

if __name__ == '__main__':
    main()
