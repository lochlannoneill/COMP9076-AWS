from utils.reading_from_user import read_range_integer
from models.User import UserManager

class App:
    MENU_OPTIONS = {
        "Login": 1,
        "Register": 2,
        "Exit": 3
    }

    def __init__(self, user_manager):
        self.user_manager = user_manager

    def display_menu(self):
        """Display the main menu options to the user."""
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
                    # TODO - Pass user_credentials to AWS handling functions if needed
                    break  # Exit the menu after successful login
            elif option == self.MENU_OPTIONS["Register"]:
                self.user_manager.register_user()
            elif option == self.MENU_OPTIONS["Exit"]:
                print("Exiting...")
                exit()
            else:
                print("Invalid menu option.")

def main():
    user_manager = UserManager()
    app = App(user_manager)
    app.handle_menu()

if __name__ == "__main__":
    main()
