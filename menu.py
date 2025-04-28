from drink import Drink

class Menu:
    def __init__(self):
        self.drinks = [
            Drink("espresso", {"water": 50, "coffee": 18}, 1.5),
            Drink("latte", {"water": 200, "milk": 150, "coffee": 24}, 2.5),
            Drink("cappuccino", {"water": 250, "milk": 100, "coffee": 24}, 3.0)
        ]

    def get_items(self):
        return ", ".join(drink.name for drink in self.drinks)

    def find_drink(self, name):
        return next((d for d in self.drinks if d.name == name), None)