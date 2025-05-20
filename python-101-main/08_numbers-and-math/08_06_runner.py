# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

miles = 10
km = miles * 1.6 # 10 miles×1.6 = 16 km
time_minutes = 30 + 30 / 60 # 30 minutes and 30 seconds
time_hours = time_minutes / 60

speed_kph = km / time_hours

print("Average speed (km/h):", speed_kph)


