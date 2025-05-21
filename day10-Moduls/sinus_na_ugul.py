import math

degrees = float(input("Enter Number: "))

radians = math.radians(degrees)
sine = math.sin(radians)

print(f"Sin({degrees}) = {round(sine, 4)}")