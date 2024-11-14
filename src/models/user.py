from os.path import join, exists
import json
from src.utils.reading_from_user import read_nonempty_string

class userManager:
    def __init__(self):
        self.file_path = join("src", "config", "passwords.json")
        self.users = self.load_users()

    def load_users(self):
        """Load existing users from the password JSON file."""
        users = {}
        if exists(self.file_path):
            with open(self.file_path, "r") as file:
                try:
                    users_list = json.load(file)
                    for user in users_list:
                        username = user["name"]
                        password = user["password"]
                        access_key = user["access key"]
                        secret_key = user["secret key"]
                        users[username] = {
                            "password": password,
                            "access_key": access_key,
                            "secret_key": secret_key
                        }
                except json.JSONDecodeError:
                    print("Error: Could not decode the JSON file.")
        return users

    def login_user(self):
        """Authenticate an existing user."""
        while True:
            username = read_nonempty_string("Username: ")
            password = read_nonempty_string("Password: ")
            valid_user = username in self.users and self.users[username]["password"] == password

            if valid_user:
                print(f"Welcome, {username}!")
                return self.users[username]
            print("Invalid username or password. Please try again.")

    def register_user(self):
        """Register a new user and add them to the password JSON file."""
        username = read_nonempty_string("Enter a new username: ")
        password = read_nonempty_string("Enter a password: ")
        access_key = read_nonempty_string("Enter your AWS Access Key ID: ")
        secret_key = read_nonempty_string("Enter your AWS Secret Access Key: ")

        # Load existing users from JSON and append new user
        with open(self.file_path, "r") as file:
            users_list = json.load(file)
        
        # Add the new user to the list
        users_list.append({
            "name": username,
            "password": password,
            "access key": access_key,
            "secret key": secret_key
        })

        # Write updated list back to the JSON file
        with open(self.file_path, "w") as file:
            json.dump(users_list, file, indent=4)
        
        print(f"User '{username}' registered successfully.")
        # Update in-memory users dictionary
        self.users[username] = {
            "password": password,
            "access_key": access_key,
            "secret_key": secret_key
        }
