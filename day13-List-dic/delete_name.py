name = input("Enter name: ")

people = [
    {"name": "Ivan", "years": 34},
    {"name": "Ivo", "years": 22},
    {"name": "Peter", "years": 56},
    {"name": "Gabriela", "years": 56},
    {"name": "Tara", "years": 44},
    {"name": "Eli", "years": 64},
    {"name": "George", "years": 24}
]

for i in people:
    if name in i['name']:
        i.pop('name', None)

    print(i)