def print_ones_digit(num):
    # The ones digit is the remainder when dividing the number by 10
    print("The ones digit is", num % 10)

def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    
    # Call the function to print the ones digit
    print_ones_digit(num)

# This is required to ensure the main function runs when the program is executed
if __name__ == '__main__':
    main()
