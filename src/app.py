from src.models.user import UserManager
from src.menu.mainMenu import mainMenu
from src.menu.awsMenu import awsMenu
from src.models.resource import Resource

class App:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.main_menu = mainMenu()
    
    def _start(self):
        """Main application loop handling authentication and AWS menu."""
        # Main menu loop
        while True:
            user_credentials = self.main_menu.handle(self.user_manager)

            # AWS menu loop
            if user_credentials:
                while True:
                    awsMenu(user_credentials).handle()

def main():
    user_manager = UserManager()
    app = App(user_manager)
    app._start()

if __name__ == "__main__":
    main()
