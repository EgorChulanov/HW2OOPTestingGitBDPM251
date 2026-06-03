import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

# 1
def test_ingredient_init():
    ing = Ingredient("Яйца", 3, "шт")
    assert ing.name == "Яйца"
    assert ing.quantity == 3.0
    assert ing.unit == "шт"

def test_ingredient_str():
    ing = Ingredient("Масло", 200, "мл")
    assert str(ing) == "Масло: 200.0 мл"

def test_ingredient_eq_same():
    ing1 = Ingredient("Сахар", 100, "г")
    ing2 = Ingredient("Сахар", 500, "г")
    assert ing1 == ing2

def test_ingredient_eq_different_name():
    ing1 = Ingredient("Соль", 10, "г")
    ing2 = Ingredient("Сахар", 10, "г")
    assert ing1 != ing2

def test_ingredient_eq_different_unit():
    ing1 = Ingredient("Вода", 500, "мл")
    ing2 = Ingredient("Вода", 500, "л")
    assert ing1 != ing2

# 2
def test_recipe_init():
    recipe = Recipe("Пицца")
    assert recipe.title == "Пицца"
    assert recipe.ingredients == []

def test_recipe_add_ingredient():
    recipe = Recipe("Паста")
    recipe.add_ingredient(Ingredient("Макароны", 300, "г"))
    assert len(recipe) == 1

def test_recipe_add_duplicate_sums():
    recipe = Recipe("Паста")
    recipe.add_ingredient(Ingredient("Макароны", 300, "г"))
    recipe.add_ingredient(Ingredient("Макароны", 200, "г"))
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 500.0

def test_recipe_scale_returns_new():
    recipe = Recipe("Паста")
    recipe.add_ingredient(Ingredient("Макароны", 300, "г"))
    scaled = recipe.scale(2)
    assert scaled is not recipe

def test_recipe_scale_quantity():
    recipe = Recipe("Паста")
    recipe.add_ingredient(Ingredient("Макароны", 300, "г"))
    scaled = recipe.scale(3)
    assert scaled.ingredients[0].quantity == 900.0

def test_recipe_scale_invalid():
    recipe = Recipe("Паста")
    with pytest.raises(ValueError):
        recipe.scale(-1)

def test_recipe_len():
    recipe = Recipe("Паста")
    recipe.add_ingredient(Ingredient("Макароны", 300, "г"))
    recipe.add_ingredient(Ingredient("Соль", 200000, "г"))
    assert len(recipe) == 2

def test_shopping_add_recipe():
    sl = ShoppingList()
    recipe = Recipe("Салат")
    recipe.add_ingredient(Ingredient("Арбуз", 1000, "г"))
    sl.add_recipe(recipe, 2)
    items = sl.get_list()
    assert len(items) == 1
    assert items[0].quantity == 2000.0

def test_shopping_add_recipe_invalid_portions():
    sl = ShoppingList()
    recipe = Recipe("Салат")
    with pytest.raises(ValueError):
        sl.add_recipe(recipe, 0)

def test_shopping_remove_recipe():
    sl = ShoppingList()
    recipe = Recipe("Компот")
    recipe.add_ingredient(Ingredient("Абрикос", 500, "г"))
    sl.add_recipe(recipe, 1)
    sl.remove_recipe("Компот")
    assert sl.get_list() == []

def test_shopping_remove_nonexistent():
    sl = ShoppingList()
    sl.remove_recipe("Нет такого")

def test_shopping_get_list_sums():
    sl = ShoppingList()
    recipe1 = Recipe("Смузи")
    recipe2 = Recipe("Десерт")
    recipe1.add_ingredient(Ingredient("Банан", 200, "г"))
    recipe2.add_ingredient(Ingredient("Банан", 300, "г"))
    sl.add_recipe(recipe1, 1)
    sl.add_recipe(recipe2, 1)
    result = sl.get_list()
    assert result[0].quantity == 500.0

def test_shopping_get_list_sorted():
    sl = ShoppingList()
    recipe = Recipe("Фруктовый салат")
    recipe.add_ingredient(Ingredient("Черешня", 100, "г"))
    recipe.add_ingredient(Ingredient("Абрикос", 200, "г"))
    sl.add_recipe(recipe, 1)
    names = [ing.name for ing in sl.get_list()]
    assert names == sorted(names)

def test_shopping_add_operator():
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    recipe = Recipe("Компот")
    recipe.add_ingredient(Ingredient("Вишня", 400, "г"))
    sl1.add_recipe(recipe, 1)
    combined = sl1 + sl2
    assert combined is not sl1
    assert combined is not sl2

def test_shopping_add_operator_original_unchanged():
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    recipe = Recipe("Компот")
    recipe.add_ingredient(Ingredient("Вишня", 400, "г"))
    sl1.add_recipe(recipe, 1)
    sl1 + sl2
    assert len(sl1._items) == 1