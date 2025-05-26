import datetime

time_wake_up = input("Enter time for wake up: ")

# Presirame vuvedenoto vreme
future = datetime.datetime.strptime(time_wake_up, "%H:%M").time()

# Tekushta data i chas
now = datetime.datetime.now()

# Kombinirame dneshnata data s vuvedeniq chas
wake_up_combinate = datetime.datetime.combine(now.date(), future)

# AKo chasut na subujdane e po-kusen ot tekushiq, znachi e bilo vchera
if wake_up_combinate > now:
    wake_up_combinate -= datetime.timedelta(days=1)

# razlika vuv vremeto
time_diff = now - wake_up_combinate

# Preobrazuvane v chasove
hours_ago = time_diff.total_seconds() / 3600

print(f"You woke up {hours_ago:.2f} hours ago.")
