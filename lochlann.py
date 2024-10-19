import os
from reading_from_user import read_nonempty_string

FILE_PASSWORDS = "passwords.txt"

# Function to load existing users from the passwords file
def load_users():
    users = {}
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, "r") as file:
            for line in file:
                if line.strip():
                    username, password, access_key, secret_key = line.strip().split("\t")
                    users[username] = {
                        "password": password,
                        "access_key": access_key,
                        "secret_key": secret_key
                    }
    return users

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
        print("\n1. Login")
        print("2. Register")
        choice = input("Select (1 or 2): ")
        
        if choice == "1":
            if user_credentials:
                print("To do: Implement user login")
        elif choice == "2":
            register_user()
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
