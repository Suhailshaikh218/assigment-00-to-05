def main():
    lst = []  # Create an empty list to store the values

    val = input("Enter a value: ")  # Get the first value
    while val:  # While the user inputs something
        lst.append(val)  # Add the value to the list
        val = input("Enter a value: ")  # Get the next value

    print("Here's the list:", lst)


# The following code is necessary to call the main function
if __name__ == '__main__':
    main()
