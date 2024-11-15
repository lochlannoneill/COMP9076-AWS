from src.models.user import UserManager
from src.menu.mainMenu import mainMenu
from src.menu.awsMenu import awsMenu
from src.models.resource import Resource

class App:
    def main(self):
        """Main application loop handling authentication and AWS menu."""
        # Main menu loop
        while True:
            user_credentials = mainMenu().handle(UserManager())

            # AWS menu loop
            if user_credentials:
                while True:
                    awsMenu(user_credentials).handle()
                    break

if __name__ == "__main__":
    app = App()
    app.main()
