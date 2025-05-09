import time

def computer_guesses():
    print("Welcome to the Reverse Guess the Number Game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").strip().lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number in {attempts} attempts.")
            break
        else:
            print("Invalid input. Please enter 'H', 'L', or 'C'.")
        time.sleep(1)

# Run the game
computer_guesses()
