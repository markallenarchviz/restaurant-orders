from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2 !
def test_dish():
    dish = Dish("Carbonara", 15.99)
    assert dish.name == "Carbonara"
    assert dish.price == 15.99

    dish1 = Dish("Carbonara", 15.99)
    dish2 = Dish("Carbonara", 15.99)
    assert hash(dish1) == hash(dish2)

    dish3 = Dish("Lasagna", 13.99)
    assert hash(dish1) != hash(dish3)

    assert dish1 == dish2

    assert dish1 != dish3

    assert repr(dish) == "Dish('Carbonara', R$15.99)"

    ingredient = Ingredient("bacon")
    dish.add_ingredient_dependency(ingredient, 1)
    print("dish.recipe após adicionar 'bacon': ", dish.recipe)
    print("Resultado do print", dish.recipe)

    assert dish.recipe.get(ingredient) == 1

    with pytest.raises(TypeError):
        Dish("Carbonara", "R$15.99")

    with pytest.raises(ValueError):
        Dish("Carbonara", -15.99)

    dish.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)
    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED,
                             Restriction.ANIMAL_MEAT}
    assert dish.get_restrictions() == expected_restrictions

    expected_ingredients = {ingredient, Ingredient("queijo mussarela")}
    assert dish.get_ingredients() == expected_ingredients
