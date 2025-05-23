try:
    month = int(input("Enter month (1-12): "))

    if 1 <= month <= 12:
        print(f"That is correct. We have 12 months in one year!")
    elif month > 12:
        print("Enter right number!")


except ValueError:
    print("Enter number 1-12, no text, no big number!")