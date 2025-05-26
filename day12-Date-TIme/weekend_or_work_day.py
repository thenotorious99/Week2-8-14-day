import datetime

date_today = datetime.datetime.today()

print(f"Today is: {date_today.strftime('%A, %Y-%m-%d')}")

day_name = date_today.strftime('%A')

if day_name in ["Saturday","Sunday"]:
    print("Today is weekend day.")
else:
    print("Today is work day.")

