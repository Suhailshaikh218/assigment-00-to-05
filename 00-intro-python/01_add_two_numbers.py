"""
Program: add2numbers
--------------------
This Python program prompts the user to enter two integers
and calculates their sum, displaying the result.
"""

def main():
    print("This program adds two numbers.")
    
    # Prompt and read first integer
    num1_input = input("Enter first number: ")
    num1 = int(num1_input)
    
    # Prompt and read second integer
    num2_input = input("Enter second number: ")
    num2 = int(num2_input)
    
    # Calculate and print the total
    total = num1 + num2
    print(f"The total is {total}.")

# Required to run the main function when the script is executed
if __name__ == '__main__':
    main()
