"""Data"""
from datetime import datetime

main_date = "2020-11-04 14:53:00"

format_date_1 = "%Y/%m/%d %H:%M:%S"
format_date_2 = "%Y/%B/%d %H:%M:%S %p"
format_date_3 = "%a %Y/%b/%d"
format_date_4 = "%A %Y/%b/%d"

date_new = datetime(2020, 11, 4, 14, 53)
date_old = datetime(2020, 1, 4, 14, 53)

delta = date_new - date_old

date_year = main_date.split(' ')[0]
date_hour = main_date.split(' ')[1]

print(date_new.strftime(format_date_1))
print(date_new.strftime(format_date_2))
print(date_new.strftime(format_date_3))
print(date_new.strftime(format_date_4))
print(f"Day of the year: {delta.days}")
print(f"Week number of the year: {date_new.isocalendar()[1]}")
print(f"Weekday: {date_new.isoweekday()}")
