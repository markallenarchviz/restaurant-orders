from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


def test_ingredient():

    ingrediente = Ingredient("frango")
    assert ingrediente.name == "frango"
    assert ingrediente.restrictions == {Restriction.ANIMAL_MEAT,
                                        Restriction.ANIMAL_DERIVED}

    assert ingrediente.__repr__() == "Ingredient('frango')"

    animal = Ingredient("carne")

    assert hash(ingrediente) != hash(animal)
    assert hash(ingrediente) == hash(Ingredient("frango"))

    assert (ingrediente == animal) is False
    assert (ingrediente == ingrediente) is True
