try:
    year = int(input("Enter which year you were born: "))

    result = 2025 - year
    print(f"You are {result} old now!")

except ValueError:
    print("Enter only numbers! No letters!")