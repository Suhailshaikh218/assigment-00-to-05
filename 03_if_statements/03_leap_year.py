def main():
    # Get the year to check from the user
    year = int(input("Please input a year: "))

    # Apply leap year rules from the Gregorian calendar
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")


# Required to call the main function when this file is run
if __name__ == '__main__':
    main()
