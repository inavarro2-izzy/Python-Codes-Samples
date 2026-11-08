# Israel Navarro
# November 8, 2026
# Problem 6: Add type and manufacturer attributes and methods to a car class.

# An attribute is information stored in an object, such as color.
# A method is a function in a class that performs an action or returns information.

class car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return (self.model + " " + str(self.year) + " " + self.color
                + " " + self.type + " " + self.manufacturer)

car1 = car("Sports", 2012, "Blue", "Coupe", "Ford")
car2 = car("Sedan", 2020, "Black", "Four-door", "Toyota")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.get_type())
print(car1.get_manufacturer())
print(car1.fullspecs())
print(car2.fullspecs())
