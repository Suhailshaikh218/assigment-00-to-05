import random

def hangman():
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming']
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    display_word = ['_' for _ in word]

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while attempts > 0 and '_' in display_word:
        print("\nWord: " + ' '.join(display_word))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    display_word[idx] = guess
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. Attempts remaining: {attempts}")

    if '_' not in display_word:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame over. The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()
