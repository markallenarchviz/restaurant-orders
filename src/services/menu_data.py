import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self._load_data(source_path)

    def _load_data(self, source_path: str):
        with open(source_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish_name = row['dish']
                dish_price = float(row['price'])
                ingredient_name = row['ingredient']
                ingredient_amount = int(row['recipe_amount'])

                dish = self._get_dish(dish_name, dish_price)
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, ingredient_amount)

    def _get_dish(self, dish_name: str, dish_price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish

        dish = Dish(dish_name, dish_price)
        self.dishes.add(dish)
        return dish
