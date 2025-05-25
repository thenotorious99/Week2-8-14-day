import datetime

date_input = input("Enter Year-Month-Date: ")


future = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()

today = datetime.date.today()

diff = future - today
print(f"{diff.days} days left")