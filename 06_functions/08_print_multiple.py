def print_multiple(message: str, repeats: int):
    # This function prints the message the specified number of times.
    for i in range(repeats):
        print(message)

def main():
    # Prompt the user for a message and number of repeats.
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the print_multiple function with the user's input
    print_multiple(message, repeats)

# This line ensures that main() is called when the script is executed.
if __name__ == '__main__':
    main()
