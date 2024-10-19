import os
from reading_from_user import read_nonempty_string
from reading_from_user import read_range_integer

FILE_PASSWORDS = "passwords.txt"

# Function to load existing users from the passwords file
def load_users():
    users = {}
    if os.path.exists(FILE_PASSWORDS):
        with open(FILE_PASSWORDS, "r") as file:
            for line in file:
                if line.strip():
                    username, password, access_key, secret_key = line.strip().split("\t")
                    users[username] = {
                        "password": password,
                        "access_key": access_key,
                        "secret_key": secret_key
                    }
    return users

# Function to authenticate an existing user
def login_user(users):
    while True:
        username = input("Username (leave blank to exit): ")
        if not username:
            print("Exiting program...")
            exit()

        password = input("Password: ")
        
        # Validate credentials
        if username in users and users[username]["password"] == password:
            print(f"Welcome, {username}!")
            return users[username]
        else:
            print("Invalid username or password. Please try again.")


# Register a new user
def register_user():
    username = read_nonempty_string("Enter a new username: ")
    password = read_nonempty_string("Enter a password: ")
    access_key = read_nonempty_string("Enter your AWS Access Key ID: ")
    secret_key = read_nonempty_string("Enter your AWS Secret Access Key: ")
    
    # Append new user to file
    with open(FILE_PASSWORDS, "a") as file:
        file.write(f"{username}\t{password}\t{access_key}\t{secret_key}\n")
    
    print(f"User '{username}' registered successfully.")

# Main function to control the login and registration flow
def main():
    users = load_users()
    
    while True:
        MENU_OPTIONS = {
            "Login": 1,
            "Register": 2
        }
        
        # Use read_range_integer with dictionary values
        choice = read_range_integer("Select valid option: ", min(MENU_OPTIONS.values()), max(MENU_OPTIONS.values()))
        
        if choice == MENU_OPTIONS["Login"]:
            if user_credentials:
                print("Welcome, {user_credentials['username']}!")
                return user_credentials
        elif choice == MENU_OPTIONS["Register"]:
            register_user()
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
