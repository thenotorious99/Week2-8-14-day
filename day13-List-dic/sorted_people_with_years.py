people = [
    {"name": "Ivan", "years": 34},
    {"name": "Ivo", "years": 22},
    {"name": "Peter", "years": 56},
    {"name": "Gabriela", "years": 66},
    {"name": "Tara", "years": 44},
    {"name": "Eli", "years": 64},
    {"name": "George", "years": 24}
]

people.sort(key=lambda k : k["years"], reverse=True)


print(people)