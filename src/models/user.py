from os.path import join, exists
from src.utils.reading_from_user import read_nonempty_string

FILE_PASSWORDS = join("src", "config", "passwords.txt")
FILE_FIELDS_COUNT = 4

class userManager:
    def __init__(self, file_path=FILE_PASSWORDS):
        self.file_path = file_path
        self.users = self.load_users()

    # COMPLETED
    def load_users(self):
        """Load existing users from the password file."""
        users = {}
        if exists(self.file_path):  # Use self.file_path instead of self.FILE_PASSWORDS
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

    # COMPLETED
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

    # COMPLETED
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
        # Update in-memory users dictionary  # TODO
        self.users[username] = {
            "password": password,
            "access_key": access_key,
            "secret_key": secret_key
        }
