try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num2 == 0:
        print("You cannot division on zero!")

    elif num1 and num2:
        result = num1 / num2
        print(result)


except ValueError:
    print("Enter valid numbers!")