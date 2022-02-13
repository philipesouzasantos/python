class Data:
    def __init__(self, dd, mm, yyyy):
        self.__dd = dd
        self.__mm = mm
        self.__yyyy = yyyy

    def formatada (self):
        print("Data formatada: {}/{}/{}".format(self.__dd, self.__mm, self.__yyyy))
