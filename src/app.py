from src.models.user import userManager
from src.menu.mainMenu import mainMenu
from src.menu.awsMenu import awsMenu
from src.models.resource import resource

class App:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.main_menu = mainMenu()
        self.aws_menu = None
        self.region = "eu-west-1"

    def _authenticate_user(self):
        """Handles user login and session creation."""
        user_credentials = self.main_menu.handle(self.user_manager)
        if user_credentials:
            # Create and return a session object after successful login
            return resource(
                region=self.region,
                key_id=user_credentials["access_key"],
                secret_key=user_credentials["secret_key"]
            )
        return None

    def _initialize_aws_menu(self, session):
        """Initialize awsMenu with the session after user authentication."""
        if session:
            self.aws_menu = awsMenu(session)
            return True
        return False

    def _run_aws_menu(self):
        """Run the AWS menu loop."""
        if not self.aws_menu:
            print("AWS Menu is not initialized.")
            return
        while True:
            if not self.aws_menu.handle():
                break

    def _start(self):
        """Main application loop handling authentication and AWS menu."""
        while True:
            session = self._authenticate_user()
            if self._initialize_aws_menu(session):
                self._run_aws_menu()
                break  # Exit after AWS menu interaction

def main():
    user_manager = userManager()  # Initialize the user manager
    app = App(user_manager)       # Initialize the App with the user manager
    app._start()                  # Start the application

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
