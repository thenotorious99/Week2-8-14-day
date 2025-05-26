import datetime

now = datetime.datetime.today()

tomorrow = now + datetime.timedelta(days=1)

print(f"Today is: {now.strftime('%A')}")
print(f"Tomorrow is: {tomorrow.strftime('%A')}")

""""
datetime.date.today() – връща днешната дата.

timedelta(days=1) – добавя 1 ден към нея.

strftime('%A') – връща името на деня от седмицата (на английски).
"""