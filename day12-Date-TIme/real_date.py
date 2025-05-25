import datetime


today = datetime.date.today()
formate_date = today.strftime("%d.%m.%y")

print(formate_date)

"""
print(today)

year = today.year
month = today.month
day = today.day

print(f"Year: {year}, Month: {month}, Day: {day}")
"""