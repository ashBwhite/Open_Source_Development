# task 1
class Window:

    __filled_up = False

    def __init__(self, width, height, filled_up):
        self.width = width
        self.height = height
        self.__filled_up = filled_up

# task 3
class Instrument:
    __issilver = False

    def __init__(self, name, manufacturar, issilver):
        self.name = name
        self.manufacturar = manufacturar
        self.__issilver = issilver

    def __str__(self):
        return "Name:" + str(self.name) + "\nManufacturar:" + str(self.manufacturar) + "\nIs it made out of silver? " + str(self.__issilver)

instrument = Instrument("Flute", "Yamaha", True)
print(instrument)