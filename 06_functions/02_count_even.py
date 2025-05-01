def count_even(lst):
    """
    Prints the number of even integers in the list.
    """
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)

def get_list_of_ints():
    """
    Prompts the user to enter integers until they press enter, and returns the list of entered integers.
    """
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Please enter a valid integer.")
        user_input = input("Enter an integer or press enter to stop: ")
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()
