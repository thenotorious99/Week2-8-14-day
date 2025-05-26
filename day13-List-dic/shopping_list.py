products = [
    {"name of product": "banana", "price": 2},
    {"name of product": "chocolate", "price": 4},
    {"name of product": "orange", "price": 1},
    {"name of product": "kiwi", "price": 10},
    {"name of product": "cake", "price": 12},
]


sum_total = sum(i['price'] for i in products)

print(f"Total sum of all products is {sum_total}")