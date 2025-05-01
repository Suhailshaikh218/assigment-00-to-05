def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Loop from 1 to num (inclusive)
        if num % i == 0:  # If i divides num with no remainder
            print(i)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)  # Call the helper function to print divisors

# This line is required to ensure main() is called
if __name__ == '__main__':
    main()