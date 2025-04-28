from utils.file_io import load_machine, save_machine
from menu import Menu

class CoffeeMachine:
    def __init__(self):
        self.resources = load_machine() or {
            "water": 500,
            "milk": 300,
            "coffee": 200
        }

        self.menu = Menu()

    def report(self):
        return {item: self.resources[item] for item in self.resources}

    def is_resource_sufficient(self, drink):
        for item, amount in drink.ingredients.items():
            if self.resources.get(item, 0) < amount:
                return False, item
        return True, None

    def make_coffee(self, drink):
        # Debug print before reducing resources
        print(f"Before making {drink.name}: {self.resources}")
        
        for item, amount in drink.ingredients.items():
            self.resources[item] -= amount
        
        # Debug print after reducing resources
        print(f"After making {drink.name}: {self.resources}")
        
        self.save()
        return True, f"Here is your {drink.name}! ☕ Enjoy!"

    def refill(self, additions):
        for item, amount in additions.items():
            self.resources[item] += amount
        self.save()

    def save(self):
        save_machine(self.resources)