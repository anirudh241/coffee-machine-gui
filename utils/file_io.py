import json
import os

USER_DB = "data/users.json"
MACHINE_DB = "data/machine.json"

def load_users():
    if not os.path.exists(USER_DB):
        return {}
    with open(USER_DB, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=2)

def load_machine():
    if not os.path.exists(MACHINE_DB):
        return None
    with open(MACHINE_DB, "r") as f:
        return json.load(f)

def save_machine(resources):
    with open(MACHINE_DB, "w") as f:
        json.dump(resources, f, indent=2)