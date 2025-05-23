try:
    kg = float(input("Enter KG number: "))
    print(f"{kg} Kg!")

except ValueError:
    print("Invalid input! No symbols, no letters!")