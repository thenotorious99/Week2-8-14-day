try:
    age = int(input("Enter your age: "))
    print(f"Your age are: {age}")

    # if age != str(age):
        # print("Wrong: Enter number!")

except ValueError:
    print("Enter number! No letter!")
