import datetime

now = datetime.datetime.today()

print(f" Today is: {now.strftime('%A, %Y-%m-%d')}") # Използваме %A за името на деня

# Изчисляваме датите за следващите 6 дни в цикъл
for i in range(1, 7): # Започваме от 1, за да получим 'утре' като първи ден
    future_day = now + datetime.timedelta(days=i)
    print(f"Day {i} after today: {future_day.strftime('%A, %Y-%m-%d')}")