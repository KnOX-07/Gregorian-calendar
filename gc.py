import datetime

# Input year from the user
year = int(input("Enter a year: "))

# Create a datetime object for January 1st of the input year
date = datetime.date(year, 1, 1)

# Get the day of the week as an integer (0 = Monday, 6 = Sunday)
day_of_week = date.weekday()

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(f"On January 1st, {year}, it was {days[day_of_week]}.")
