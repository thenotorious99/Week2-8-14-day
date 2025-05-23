try:
    num = float(input("Enter price on product: "))

    result = num * 1.20

    print(f"Price with 20% more {result:.2f}")

except ValueError:
    print("Try with number!")



