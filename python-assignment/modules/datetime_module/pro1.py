from datetime import datetime 

# Print the current date and time using the datetime module.
now=datetime.now()
print("Current date and time:", now)

# Print only the current date.
current_date=now.date()
print("current date:",current_date)

# Print only the current time.
current_time=now.time()
print("current_time:",current_time)

# Extract and print the hour, minute, and second from the current time.
print(now.hour)
print(now.minute)
print(now.second)