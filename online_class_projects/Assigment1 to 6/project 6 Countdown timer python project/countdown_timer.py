import time

def countdown_timer():
    print("Welcome to the Countdown Timer!")
    try:
        total_seconds = int(input("Enter the time in seconds: "))
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        return

    if total_seconds <= 0:
        print("Please enter a positive number of seconds.")
        return

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        total_seconds -= 1

    print("00:00")
    print("Time's up!")

if __name__ == "__main__":
    countdown_timer()
