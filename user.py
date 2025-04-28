# user.py
import json

class User:
    def __init__(self, username, data):
        self.username = username
        self.balance = data.get("balance", 0)
        self.drinks = data.get("drinks", {})

    def charge(self, cost):
        if self.balance < cost:
            return False
        self.balance -= cost
        return True

    def add_balance(self, amount):
        self.balance += amount

    def record_drink(self, drink_name):
        self.drinks[drink_name] = self.drinks.get(drink_name, 0) + 1

    def get_data(self):
        return {
            "balance": self.balance,
            "drinks": self.drinks
        }

class UserManager:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            with open('data/users.json', 'r') as f:
                users_data = json.load(f)  # Load data from the file

                # Check if the data is a dictionary (as your JSON has usernames as keys)
                if isinstance(users_data, dict):
                    # Convert the dictionary into a list of User objects
                    return {username: User(username, data) for username, data in users_data.items()}
                else:
                    return {}  # Return empty if the structure isn't what we expect
        except FileNotFoundError:
            return {}  # Return empty if the file does not exist

    def save_users(self):
        with open('data/users.json', 'w') as f:
            # Save users as a list of dictionaries
            json.dump({username: user.get_data() for username, user in self.users.items()}, f, indent=4)

    def get_user(self, username):
        # If user doesn't exist, create a new user with default balance
        if username not in self.users:
            new_user = User(username, {"balance": 5, "drinks": {}})
            self.users[username] = new_user
            self.save_users()
        return self.users[username]

    def update_user(self, user):
        self.users[user.username] = user
        self.save_users()
