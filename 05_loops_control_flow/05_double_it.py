def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Double the number until it is 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)


# Required to call the main function
if __name__ == '__main__':
    main()
