import datetime

now = datetime.datetime.now()
today_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%H:%M:%S")

filename = f"{today_str}_log.txt"

with open(filename, "a") as file:
    file.write(f"Program started at {time_str}" + "\n")

print(f"Logged start at {time_str}")