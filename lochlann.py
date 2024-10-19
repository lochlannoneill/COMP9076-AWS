import os
from reading_from_user import read_nonempty_string

FILE_PASSWORDS = "passwords.txt"

# Main function to control the login and registration flow
def main():
    while True:
        print("\n1. Login")
        print("2. Register")
        choice = input("Select (1 or 2): ")
        
        if choice == "1":
            if user_credentials:
                print("To do: Implement user login")
        elif choice == "2":
            print("To do: Implement user registration")
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
