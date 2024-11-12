from src.utils.reading_from_user import read_range_integer

class mainMenu:
    def _display(self):
        print("\nMain Menu")
        MENU_OPTIONS = {
            "Login": 1,
            "Register": 2,
            "Exit": 3
        }
        for option, number in self.MENU_OPTIONS.items():
            print(f"{number}. {option}")

    def handle(self, user_manager):
        while True:
            self._display()
            option = read_range_integer(
                "Select from menu: ",
                min(self.MENU_OPTIONS.values()),
                max(self.MENU_OPTIONS.values())
            )

            if option == self.MENU_OPTIONS["Login"]:
                return user_manager.login_user()
            elif option == self.MENU_OPTIONS["Register"]:
                user_manager.register_user()
            elif option == self.MENU_OPTIONS["Exit"]:
                print("Exiting...")
                exit()
