import random

def main():
    # Generate a random number between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Initial guess from the user
    guess = int(input("Enter a guess: "))
    
    # Loop until the correct number is guessed
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        # Prompt for a new guess
        guess = int(input("Enter a new guess: "))
    
    # Congratulate the user
    print("Congrats! The number was:", secret_number)

if __name__ == '__main__':
    main()