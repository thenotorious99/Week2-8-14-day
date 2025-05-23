try:
    number1 = int(input("Enter first number: "))

    total = number1 ** 2
    print(f"Total is: {total}")

except ValueError:
    print("Wrong! Try again")

