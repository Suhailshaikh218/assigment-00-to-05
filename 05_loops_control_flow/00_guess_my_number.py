import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    
    # Loop until the user guesses the correct number
    while guess != secret_number:
        if guess < secret_number:  # If the guess is too low
            print("Your guess is too low")
        else:  # If the guess is too high
            print("Your guess is too high")
            
        print()  # Print an empty line to tidy up the console for new guesses
        guess = int(input("Enter a new guess: "))  # Get a new guess from the user
        
    print(f"Congrats! The number was: {secret_number}")
    
if __name__ == '__main__':
    main()
