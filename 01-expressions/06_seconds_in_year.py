"""
Program: seconds_in_year
-------------------------
This program calculates the number of seconds in a year using constants for the number of days in a year,
hours in a day, minutes in an hour, and seconds in a minute.
"""

# Define useful constants to make the math cleaner and more readable
DAYS_PER_YEAR: int = 365          # Number of days in a year
HOURS_PER_DAY: int = 24           # Number of hours in a day
MINUTES_PER_HOUR: int = 60        # Number of minutes in an hour
SECONDS_PER_MINUTE: int = 60      # Number of seconds in a minute

def main():
    # Calculate the total number of seconds in a year using the constants
    seconds_in_year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    
    # Display the result in a nice formatted print statement
    print(f"There are {seconds_in_year} seconds in a year!")

# This line calls the main function when the script is run directly
if __name__ == '__main__':
    main()
