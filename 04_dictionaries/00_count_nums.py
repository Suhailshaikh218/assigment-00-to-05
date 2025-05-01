def get_user_numbers():
    """
    Prompt the user to input numbers, store them in a list, and return the list.
    Input ends when the user provides a blank line.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers

def count_nums(num_lst):
    """
    Count the frequency of each number in the list using a dictionary.
    Returns the dictionary with number frequencies.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_counts(num_dict):
    """
    Print how many times each number appears.
    """
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")

def main():
    """
    Orchestrates the collection, counting, and printing of number frequencies.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

# This line ensures main() runs when the script is executed
if __name__ == '__main__':
    main()
