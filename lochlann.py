import os
from reading_from_user import read_nonempty_string, read_range_integer

FILE_PASSWORDS = "passwords.txt"
FILE_FIELDS_COUNT = 4

class UserManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        """Load existing users from the password file."""
        users = {}
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                for line in file:
                    stripped_line = line.strip()
                    if stripped_line:
                        parts = stripped_line.split()
                        if len(parts) == FILE_FIELDS_COUNT:
                            username, password, access_key, secret_key = parts
                            users[username] = {
                                "password": password,
                                "access_key": access_key,
                                "secret_key": secret_key
                            }
                        else:
                            print(f"Skipping line due to incorrect format: {stripped_line}")
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
        """Register a new user and add them to the password file."""
        username = read_nonempty_string("Enter a new username: ")
        password = read_nonempty_string("Enter a password: ")
        access_key = read_nonempty_string("Enter your AWS Access Key ID: ")
        secret_key = read_nonempty_string("Enter your AWS Secret Access Key: ")

        # Append new user to file
        with open(self.file_path, "a") as file:
            file.write(f"\n{username}\t{password}\t{access_key}\t{secret_key}")
        
        print(f"User '{username}' registered successfully.")
        # Update in-memory users dictionary
        self.users[username] = {
            "password": password,
            "access_key": access_key,
            "secret_key": secret_key
        }

class App:
    MENU_OPTIONS = {
        "Login": 1,
        "Register": 2
    }

    def __init__(self, user_manager):
        self.user_manager = user_manager

    def display_menu(self):
        """Display the main menu options to the user."""
        print("Press 'ctrl+c' to exit.")
        for option, number in self.MENU_OPTIONS.items():
            print(f"{number}. {option}")

    def handle_menu(self):
        """Handle the user's menu selection."""
        while True:
            self.display_menu()
            option = read_range_integer(
                "Select from menu: ",
                min(self.MENU_OPTIONS.values()),
                max(self.MENU_OPTIONS.values())
            )

            if option == self.MENU_OPTIONS["Login"]:
                user_credentials = self.user_manager.login_user()
                if user_credentials:
                    # Pass user_credentials to AWS handling functions if needed
                    break  # Exit the menu after successful login
            elif option == self.MENU_OPTIONS["Register"]:
                self.user_manager.register_user()
            else:
                print("Invalid menu option.")

def main():
    user_manager = UserManager(FILE_PASSWORDS)
    app = App(user_manager)
    app.handle_menu()

if __name__ == "__main__":
    main()
