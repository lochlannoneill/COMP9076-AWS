import boto3
from models.User import UserManager
from models.EC2 import EC2
from Menu import MainMenu, AwsMainMenu, EC2Menu

class App:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.main_menu = MainMenu()
        self.aws_main_menu = AwsMainMenu()
        self.ec2_menu = EC2Menu()

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
            if not self.aws_main_menu.handle(ec2_service):
                break

            while True:
                # Display EC2-specific menu and handle it
                if not self.ec2_menu.handle(ec2_service):
                    break
