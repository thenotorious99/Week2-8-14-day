try:
    num = int(input("Enter number: "))

    if num % 2 == 0:
        print(f"This number is {num} even!")
    else:
        print(f"This number {num}  is odd!")
except ValueError:
    print("Invalid input")
