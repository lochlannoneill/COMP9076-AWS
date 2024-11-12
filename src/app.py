from src.models.user import userManager
from src.models.ec2 import EC2Controller
from src.menu.mainMenu import mainMenu
from src.menu.awsMenu import awsMenu
from src.models.resource import resource  # Import the resource class

class App:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.main_menu = mainMenu()
        self.aws_menu = awsMenu()

    def _start(self):
        # Main Menu
        while True:
            user_credentials = self.main_menu.handle(self.user_manager)
            if user_credentials:
                aws_resource = resource(
                    region="eu-west-1",
                    key_id=user_credentials["access_key"],
                    secret_key=user_credentials["secret_key"]
                )
            break

        # EC2 Service
        ec2 = aws_resource.get_ec2_resource()
        ec2_service = EC2Controller(ec2)
        while True:
            if not self.aws_menu.handle(ec2_service):
                break

def main():
    user_manager = userManager()  # Initialize the user manager
    app = App(user_manager)       # Initialize the App with the user manager
    app._start()                     # Start the application

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
