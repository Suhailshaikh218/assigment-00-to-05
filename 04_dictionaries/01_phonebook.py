def read_phone_numbers():
    """
    Ask the user for names and numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Initialize empty dictionary

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number  # Store name-number pair

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names and their associated phone numbers.
    """
    print("\nPhonebook entries:")
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")


def lookup_numbers(phonebook):
    """
    Allow the user to look up numbers in the phonebook by name.
    Continues until the user enters a blank line.
    """
    print("\nLookup mode:")
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name in phonebook:
            print(phonebook[name])
        else:
            print(f"{name} is not in the phonebook")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

# This line ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()
