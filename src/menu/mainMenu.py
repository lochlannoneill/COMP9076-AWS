from src.utils.reading_from_user import read_range_integer

class mainMenu:
    def __init__(self):
        self.options = {
            "Login": 1,
            "Register": 2,
            "Exit": 3
        }

    def _display(self):
        """Display the main menu options."""
        print("\nMain Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, user_manager):
        """Handle the main menu interaction."""
        while True:
            self._display()
            choice = read_range_integer(
                "Select from menu: ",
                min(self.options.values()),
                max(self.options.values())
            )

            if choice == self.options["Login"]:
                return user_manager.login_user()
            elif choice == self.options["Register"]:
                user_manager.register_user()
            elif choice == self.options["Exit"]:
                print("Exiting...")
                exit()
