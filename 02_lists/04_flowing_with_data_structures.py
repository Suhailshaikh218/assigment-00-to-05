def add_three_copies(my_list, data):
    # List is mutable, so appending directly affects the original list
    for _ in range(3):
        my_list.append(data)

# ===== No need to edit code past this point =====

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()
