people = [
    {"name": "Ivan", "years": 34},
    {"name": "Ivo", "years": 22},
    {"name": "Peter", "years": 56},
    {"name": "Gabriela", "years": 66},
    {"name": "Tara", "years": 44},
    {"name": "Eli", "years": 64},
    {"name": "George", "years": 24}
]

# obshta suma na godinite
years_total = sum(i['years'] for i in people)

# Broi hora
count = len(people)

# sredna vuzrast
average = years_total / count

# zakruglqme sbora do 2 chislo
print(f"Middle years: {round(average, 2)}")

