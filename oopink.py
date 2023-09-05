class Auto:
    def __init__(self, brand: str, year: int):
        self._brand = ""
        self._year = 0

        self.brand = brand
        self.year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if value:
            self._brand = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, int) and value > 0:
            self._year = value

car = Auto("Toyota", 2021)

print(car.brand)
print(car.year)
