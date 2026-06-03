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
    recipe.add_ingredient(Ingredient("Соль", 5, "г"))
    assert len(recipe) == 2