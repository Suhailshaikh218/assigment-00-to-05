def main():
    # Dictionary containing fruits and their price per unit
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0

    # Loop through each fruit and ask how many the user wants to buy
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input(f"How many ({fruit_name}) do you want?: "))
        total_cost += price * amount_bought

    # Print total cost
    print(f"Your total is ${total_cost}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
