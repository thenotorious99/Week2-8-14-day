user_year = int(input("Enter years: "))
user = {
    "name": "Ivan",
    "years": 17
}

if user_year <= 18:
    print("The user is minor")
else:
    print("The user is adult")
