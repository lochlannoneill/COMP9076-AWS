from src.models.user import UserManager
from src.menu.mainMenu import mainMenu
from src.menu.awsMenu import awsMenu
from src.models.resource import Resource

class App:
    def __init__(self):
        self.main_menu = mainMenu()
    
    def _start(self):
        """Main application loop handling authentication and AWS menu."""
        # Main menu loop
        while True:
            user_credentials = self.main_menu.handle(UserManager())

            # AWS menu loop
            if user_credentials:
                while True:
                    awsMenu(user_credentials).handle()
                    break

def main():
    app = App()
    app._start()

if __name__ == "__main__":
    main()
