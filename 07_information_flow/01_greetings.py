def greet(name: str) -> str:
    """Return a greeting message with the given name."""
    return f"Greetings {name.strip()}!"

def main():
    name = input("What's your name? ").strip()
    print(greet(name))

if __name__ == '__main__':
    main()