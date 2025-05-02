def main():
    # Prompt the user to enter a number and convert it to an integer
    num = int(input("Enter a number: "))
    curr_value = num
    
    # Loop to double the current value until it is 100 or more
    while curr_value < 100:
        print(curr_value)
        curr_value = curr_value * 2
    
    # Print the final value if it was doubled past 100
    if curr_value >= 100:
        print(curr_value)

if __name__ == '__main__':
    main()