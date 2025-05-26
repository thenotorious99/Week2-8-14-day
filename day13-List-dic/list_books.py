author = input("Enter author on book: ")


books = [
    {"author": "David Goggins", "books": "Can't Hurt Me"},
    {"author": "Jon Lopes", "books": "Never give up"},
    {"author": "Michel Cors", "books": "Rich dad"},
    {"author": "Jany Roddary", "books": "Open your mindset"},

]

for i in books:
    if author == i["author"]:
        print(f"This author has that book: {i['books']}")