import datetime

now = datetime.datetime.now()
filename = now.strftime("%Y-%m-%d") + ".txt"

with open(filename, "w") as file:
    file.write(str(now))