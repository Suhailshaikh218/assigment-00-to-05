def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    # Example test cases
    print(in_range(5, 1, 10))  # True, 5 is between 1 and 10
    print(in_range(0, 1, 10))  # False, 0 is less than 1
    print(in_range(10, 1, 10))  # True, 10 is equal to the upper bound

if __name__ == '__main__':
    main()
