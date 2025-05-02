def initialize_list():
    return ['apple', 'banana', 'orange', 'grape', 'pineapple']

def access_element(lst, index):
    if index < 0 or index >= len(lst):
        return "Index out of range"
    return lst[index]

def modify_element(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return "Index out of range"
    lst[index] = new_value
    return lst

def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start > end:
        return "Invalid indices"
    return lst[start:end]

def main():
    lst = initialize_list()
    print("Initial list:", lst)
    
    while True:
        print("\nOperations:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            index = int(input("Enter the index to access: "))
            result = access_element(lst, index)
            print("Element at index", index, ":", result)
        
        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(lst, index, new_value)
            if isinstance(result, str):
                print(result)
            else:
                print("Updated list:", result)
        
        elif choice == '3':
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(lst, start, end)
            if isinstance(result, str):
                print(result)
            else:
                print("Sliced list:", result)
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()