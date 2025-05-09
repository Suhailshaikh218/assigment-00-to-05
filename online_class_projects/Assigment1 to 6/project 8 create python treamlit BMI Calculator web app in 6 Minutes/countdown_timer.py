import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')  # overwrite the same line
        time.sleep(1)  # pause for 1 second
        seconds -= 1
    print("Time's up!")  # notify when the countdown ends

# Example usage
if __name__ == "__main__":
    try:
        # User input for the countdown time in seconds
        total_seconds = int(input("Enter the time in seconds for the countdown: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid number.")
