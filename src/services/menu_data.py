# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set(self._read_csv(source_path))

    def _read_csv(self, source_path):
        with open(source_path, encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",")
            dishes = {}
            for row in data:
                dish_name = row["dish"]
                if dish_name not in dishes:
                    dish = Dish(dish_name, float(row["price"]))
                    dishes[dish_name] = dish
                ingredient = Ingredient(row["ingredient"])
                dishes[dish_name].add_ingredient_dependency(
                    ingredient, int(row["recipe_amount"])
                )

        return dishes.values()
