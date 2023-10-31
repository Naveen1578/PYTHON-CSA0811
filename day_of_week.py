from datetime import datetime

def day_of_week(day: int, month: int, year: int) -> str:
    date = datetime(year, month, day)
    return date.strftime("%A")

day = 31
month = 8
year = 2019
print(day_of_week(day, month, year))
