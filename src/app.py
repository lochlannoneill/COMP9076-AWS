from src.models.user import userManager
from src.menu.mainMenu import mainMenu
from src.menu.awsMenu import awsMenu
from src.models.resource import Resource

class App:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.main_menu = mainMenu()
        self.aws_menu = None

    def _create_aws_session(self, user_credentials):
        """Create an AWS session based on the user's credentials."""
        return Resource(
            region="eu-west-1",  # TODO - should i prompt for region when registering?
            key_id=user_credentials["access_key"],
            secret_key=user_credentials["secret_key"]
        )
    
    def _start(self):
        """Main application loop handling authentication and AWS menu."""
        while True:
            user_credentials = self.main_menu.handle(self.user_manager)

            if user_credentials:
                self.aws_menu = awsMenu(self._create_aws_session(user_credentials))
                while True:
                    if not self.aws_menu.handle():
                        break


def main():
    user_manager = userManager()
    app = App(user_manager)
    app._start()

if __name__ == "__main__":
    main()
