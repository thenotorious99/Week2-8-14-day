try:
    num = int(input("Enter number: "))

    if num > 0:
        print(f"This number {num} is positive!")

    elif num < 0:
        print(f"This number {num} negative!")

    elif num == 0:
        print(f"This number {num} is zero!")

except ValueError:
    print("Enter real number!")