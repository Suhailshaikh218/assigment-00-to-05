ADULT_AGE: int = 18  # U.S. age

def is_adult(age: int) -> bool:
    """Check if a person is an adult based on their age."""
    return age >= ADULT_AGE  # Directly return the boolean result

########## No need to edit code beyond this point :) ##########

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == "__main__":
    main()