# Constant sentence starter
SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    # Get user inputs
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Combine the inputs with the sentence starter and print the result
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# This is the standard Python entry point
if __name__ == '__main__':
    main()
