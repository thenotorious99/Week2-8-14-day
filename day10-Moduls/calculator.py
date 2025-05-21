import main

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
symbol = input("Enter symbol: +, -, *, /: ")

if symbol == "+":
    print(f"Result:", main.add(num1, num2))

elif symbol == "-":
    print(f"Result:", main.subtract(num1, num2))

elif symbol == "*":
    print(f"Result:", main.multiply(num1, num2))

elif symbol == "/":
    print(f"Result:", main.devide(num1, num2))
else:
    print("Invalid operator")






