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


class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for ingredient in scaled.ingredients:
            self._items.append((ingredient, recipe.title))
    def remove_recipe(self, title):
        new_items = []
        for ing, t in self._items:
            if t != title:
                new_items.append((ing, t))
        self._items = new_items

    def get_list(self):
        totals = {}
        for ing, t in self._items:
            key = (ing.name, ing.unit)
            if key in totals:
                totals[key] += ing.quantity
            else:
                totals[key] = ing.quantity
        result = []
        for (name, unit), qty in totals.items():
            result.append(Ingredient(name, qty, unit))
        for i in range(len(result)):
            for j in range(i + 1, len(result)):
                if result[i].name > result[j].name:
                    result[i], result[j] = result[j], result[i]
        return result

    def __add__(self, list2):
        new_list = ShoppingList()
        new_list._items = self._items +  list2._items
        return new_list