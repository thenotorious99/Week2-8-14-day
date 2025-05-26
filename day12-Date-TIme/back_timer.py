import datetime

# Pitame za broi minuti
minutes_input = int(input("Enter minutes: "))

# Vremeto sega
now = datetime.datetime.now()

# Izchislqvame krainiq chas
end_time = now + datetime.timedelta(minutes=minutes_input)

# Formatirane krainiq chas
end_time_str = end_time.strftime("%H:%M")

print(f"Time will be down {end_time_str}")