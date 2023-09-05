class Calendar:
    __slots__ = ['_day', '_month', '_year']

    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value


date = Calendar(1, 9, 2023)
print(date.day)
print(date.month)
print(date.year)
