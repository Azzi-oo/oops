class CoordValue:
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

coordX = CoordValue("coordX")
coordY = CoordValue("coordY")



class NoDataDescr:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return "NoDataDescr __get__"

noData = NoDataDescr()
# pt.noData = "hello"
