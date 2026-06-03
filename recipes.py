class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return self.name + ": " + str(self.quantity) + " " + self.unit

    def __repr__(self):
        return "Ingredient('" + self.name + "', " + str(self.quantity) + ", '" + self.unit + "')"

    def __eq__(self, ingredient2):
        return self.name == ingredient2.name and self.unit == ingredient2.unit