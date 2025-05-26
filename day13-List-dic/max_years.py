from collections import Counter

people = [
    {"name": "Ivan", "years": 34},
    {"name": "Ivo", "years": 22},
    {"name": "Peter", "years": 56},
    {"name": "Gabriela", "years": 66},
    {"name": "Tara", "years": 44},
    {"name": "Eli", "years": 64},
    {"name": "George", "years": 24}
]

years_list = [person["years"] for person in people]

max_years = max(years_list)

print(f"Max year: {max_years}")