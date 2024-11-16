from os.path import join, exists
from src.utils.reading_from_user import read_nonempty_string

class UserManager:
    def __init__(self):
        self.file_path = join("src", "config", "passwords.txt")
        self.line_tabcount = 4  # Number of fields in each line in passwords.txt
        self.users = self.load_users()

    def load_users(self):
        """Load existing users from the passwords.txt file."""
        users = {}
        if not exists(self.file_path):
            print(f"File not found '{self.file_path}'")
            return users

        try:
            with open(self.file_path, "r") as file:
                for line_number, line in enumerate(file, start=1):
                    # Clean up the line and split by tab
                    parts = line.strip().split("\t")
                    if len(parts) == self.line_tabcount:
                        username, password, access_key, secret_key = parts
                        users[username] = {
                            "password": password,
                            "access_key": access_key,
                            "secret_key": secret_key
                        }
                    else:
                        logging.warning(f"Line {line_number} in {self.file_path} is malformed: {line.strip()}")
        except Exception as e:
            print(e)

        return users

    def login(self):
        """Authenticate an existing user."""
        while True:
            username = read_nonempty_string("Username: ")
            password = read_nonempty_string("Password: ")
            valid_user = username in self.users and self.users[username]["password"] == password

            if valid_user:
                print(f"Welcome, {username}!")
                return self.users[username]
            print("Invalid username or password. Please try again.")

    def register(self):
        """Register a new user and add them to the passwords.txt file."""
        username = read_nonempty_string("Enter a new username: ")
        password = read_nonempty_string("Enter a password: ")
        access_key = read_nonempty_string("Enter your AWS Access Key ID: ")
        secret_key = read_nonempty_string("Enter your AWS Secret Access Key: ")

        # Load existing users from the file
        with open(self.file_path, "r") as file:
            users_list = file.readlines()

        # Append the new user to the list
        with open(self.file_path, "a") as file:
            file.write(f"{username}\t{password}\t{access_key}\t{secret_key}\n")
        
        print(f"User '{username}' registered successfully.")
        # Update in-memory users dictionary
        self.users[username] = {
            "password": password,
            "access_key": access_key,
            "secret_key": secret_key
        }
