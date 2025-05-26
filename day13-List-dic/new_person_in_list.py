names_ass = [
    {"name": "Ivan", "years": 4},
    {"name": "Ivo", "years": 2},
    {"name": "Peter", "years": 6},
    {"name": "Gabriela", "years": 6},
    {"name": "George", "years": 5}
]

new_names = input("Enter new name: ")
years = int(input("Enter years: "))

new_person = {"name": new_names, "years": years}

names_ass.append(new_person)

for people in names_ass:
    print(people)



