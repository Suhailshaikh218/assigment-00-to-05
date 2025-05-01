MAX_LENGTH : int = 3  # Maximum allowed length for the list

def shorten(lst):
    """Removes elements from the end of the list until it is MAX_LENGTH long."""
    while len(lst) > MAX_LENGTH:  # While the list is longer than MAX_LENGTH
        last_elem = lst.pop()  # Remove the last element
        print(last_elem)  # Print the element that was removed

# The following function is to get the list of elements from the user
def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    shorten(lst)  # Call the shorten function to reduce the list to MAX_LENGTH

if __name__ == '__main__':
    main()  # Start the program