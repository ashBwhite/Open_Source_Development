# task 1
class Home:
    def __init__(self, address='', num_household=0, area=0):
        self._address = address
        self._num_household = num_household
        self._area = area

    def set_address(self, address):
        self._address = address

    def set_household(self, household):
        self._num_household = household

    def set_area(self, area):
        self._area = area

    def get_address(self):
        return self._address

    def get_household(self):
        return self._num_household

    def get_area(self):
        return self._area

    def __str__(self):
        return f'House is located on {self._address} I live with {self._num_household} people and area of my house is {self._area}sqft'.format(
            self=self)


myHome = Home('123 Main Street', 5, 789)

print(myHome)


# task 2
class Apartment(Home):
    def __init__(self, address, num_household, area, year_built, floor):
        Home.__init__(self, address, num_household, area)
        self.year = year_built
        self.floor = floor

    def __str__(self):
        return f"This building has built on {self.year}, and I live in {self.floor}th floor".format(self=self)


x = Apartment('123 Main Street', 5, 789, 2018, 15)

print(x)
