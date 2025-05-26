age = int(input("Enter person age: "))

people = [
    {"name": "Ivan", "years": 34},
    {"name": "Ivo", "years": 22},
    {"name": "Peter", "years": 56},
    {"name": "Gabriela", "years": 56},
    {"name": "Tara", "years": 44},
    {"name": "Eli", "years": 64},
    {"name": "George", "years": 24}
]

count = 0

for person in people:
    if age == person["years"]:
        print(f"{person['name']} is {age} years old")
        count += 1

if count > 1:
    print(f"{count} people are {age} age.")
elif count == 1:
    print(f"One person is on {age} age.")
else:
    print(f"Don't have person on this {age} age.")