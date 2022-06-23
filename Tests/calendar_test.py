"""Calendar"""
from calendar import Calendar


class MyCalendar(Calendar):
    """Calendar new"""

    def __init__(self):
        super().__init__()

    def count_weekday_in_year(self, year, day):
        """New method"""
        number = 0
        for month in range(1, 13):
            for data in self.monthdays2calendar(year, month):
                for day_tuple in data:

                    if day_tuple[0] == 0:
                        continue

                    if day_tuple[1] == day:
                        number += 1

        return number

cal = MyCalendar()
print(cal.count_weekday_in_year(2000, 6))
