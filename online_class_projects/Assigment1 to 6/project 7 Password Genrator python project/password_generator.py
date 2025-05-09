import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True, use_uppercase=True, use_lowercase=True):
    # Define the possible characters for the password
    characters = ''
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print(f"Generated password: {password}")
