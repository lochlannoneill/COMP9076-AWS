import boto3
from models.user import userManager
from models.ec2 import ec2
from app.menu import mainMenu, awsMenu, ec2Menu

class App:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.main_menu = mainMenu()
        self.aws_menu = awsMenu()
        self.ec2_menu = ec2Menu()

    def run(self):
        while True:
            # Display and handle the main menu
            user_credentials = self.main_menu.handle(self.user_manager)
            if user_credentials:
                session = boto3.Session(
                    aws_access_key_id=user_credentials["access_key"],
                    aws_secret_access_key=user_credentials["secret_key"]
                )
                self.aws_menu(session)

    def aws_menu(self, session):
        REGION = "eu-west-1" # TODO - should this be user input ???
        ec2_service = EC2(session, REGION)
        
        while True:
            # Display AWS main menu and handle it
            if not self.aws_menu.handle(ec2_service):
                break

            while True:
                # Display EC2-specific menu and handle it
                if not self.ec2_menu.handle(ec2_service):
                    break

def main():
    user_manager = userManager()  # Initialize the user manager
    app = App(user_manager)       # Initialize the App with the user manager
    app.run()                     # Start the application

if __name__ == "__main__":
    main()  # Run the main function when the script is executed