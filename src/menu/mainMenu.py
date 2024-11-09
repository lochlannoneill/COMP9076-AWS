from utils.reading_from_user import read_range_integer

class mainMenu:
    MENU_OPTIONS = {
        "Login": 1,
        "Register": 2,
        "Exit": 3
    }

    def display(self):
        print("\nMain Menu")
        for option, number in self.MENU_OPTIONS.items():
            print(f"{number}. {option}")

    def handle(self, user_manager):
        while True:
            self.display()
            choice = read_range_integer(
                "Select from menu: ",
                min(self.MENU_OPTIONS.values()),
                max(self.MENU_OPTIONS.values())
            )

            if choice == self.MENU_OPTIONS["Login"]:
                return user_manager.login_user()
            elif choice == self.MENU_OPTIONS["Register"]:
                user_manager.register_user()
            elif choice == self.MENU_OPTIONS["Exit"]:
                print("Exiting...")
                exit()
            else:
                print("Invalid menu choice.")
