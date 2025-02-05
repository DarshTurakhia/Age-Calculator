from datetime import datetime

def calculate_age(name, birthdate):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    now = datetime.now()
    delta = now - birthdate

    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60

    return f"Congratulations {name} on surviving {years} years, {months} months, {days} days, {hours} hours, and {minutes} minutes."

name = input("Enter your name: ")
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
print(calculate_age(name, birthdate))
