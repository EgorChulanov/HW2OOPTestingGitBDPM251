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


class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients
    def add_ingredient(self, ingredient):
        for existing in self.ingredients:
            if existing == ingredient:
                existing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        try:
            return float(ratio) > 0
        except (TypeError, ValueError):
            return False

    def scale(self, ratio):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным числом")
        new_ingredients = []
        for ing in self.ingredients:
            new_ing = Ingredient(ing.name, ing.quantity * ratio, ing.unit)
            new_ingredients.append(new_ing)
        return Recipe(self.title, new_ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        result = "Рецепт: " + self.title + " | "
        for ing in self.ingredients:
            result += str(ing) + " , "
        return result