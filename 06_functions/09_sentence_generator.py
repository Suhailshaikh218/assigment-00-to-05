def make_sentence(word, part_of_speech):
    # Check part of speech and print appropriate sentence
    if part_of_speech == 0:
        # noun
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        # verb
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        # adjective
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        # Invalid part of speech (not 0, 1, or 2)
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    # Get the word from the user
    word = input("Please type a noun, verb, or adjective: ")
    
    # Ask the user for the part of speech
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Call make_sentence to generate the sentence based on the part of speech
    make_sentence(word, part_of_speech)

# Ensure the main function is called when the program is executed
if __name__ == '__main__':
    main()
