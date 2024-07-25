import random

class De:
    def __init__(self, minimum, maximum):
        self.__minimum = minimum
        self.__maximum = maximum

    @property
    def minimum(self):
        return self.__minimum

    @property
    def maximum(self):
        return self.__maximum

    def lance(self):
        return random.randint(self.__minimum, self.__maximum)
