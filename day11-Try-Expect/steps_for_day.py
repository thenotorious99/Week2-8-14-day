try:
    steps = int(input("Enter how many steps you made today: "))

    print(f"Today I made {steps} steps.")

except ValueError:
    print("Please enter number!")