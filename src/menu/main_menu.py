from src.models.user import UserManager
from src.utils.reading_from_user import read_range_integer

class MainMenu:
    def __init__(self):
        self.options = {
            "Login": 1,
            "Register": 2,
            "Exit": 3
        }

    def _display(self):
        """Display the main menu options."""
        print("Main Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self):
        """Handle the main menu interaction."""
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))

            if choice == self.options["Login"]:
                return UserManager().login()
            elif choice == self.options["Register"]:
                UserManager().register()
            elif choice == self.options["Exit"]:
                print("Exiting...")
                exit()
