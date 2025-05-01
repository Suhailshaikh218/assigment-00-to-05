def main():
    # Loop through numbers from 10 to 19
    for i in range(10, 20):
        if is_odd(i):  # Check if the number is odd
            print(f"{i} odd")
        else:  # If the number is even
            print(f"{i} even")

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    remainder = value % 2  # 0 if the value is divisible by 2, 1 if it's not
    return remainder == 1  # Returns True if the value is odd

# The following line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
