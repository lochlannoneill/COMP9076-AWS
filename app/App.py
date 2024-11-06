import boto3
from utils.reading_from_user import read_range_integer
from models.User import UserManager
from models.EC2 import EC2

class App:
    MENU_OPTIONS = {
        "Login": 1,
        "Register": 2,
        "Exit": 3
    }

    def __init__(self, user_manager):
        self.user_manager = user_manager

    def display_menu(self):
        """Display the main menu options to the user."""
        for option, number in self.MENU_OPTIONS.items():
            print(f"{number}. {option}")

    def handle_menu(self):
        """Handle the user's menu selection."""
        while True:
            self.display_menu()
            option = read_range_integer(
                "Select from menu: ",
                min(self.MENU_OPTIONS.values()),
                max(self.MENU_OPTIONS.values())
            )

            if option == self.MENU_OPTIONS["Login"]:
                user_credentials = self.user_manager.login_user()
                if user_credentials:
                    session = boto3.Session(
                        aws_access_key_id=user_credentials["access_key"],
                        aws_secret_access_key=user_credentials["secret_key"]
                    )
                    self.aws_main_menu(session)
            elif option == self.MENU_OPTIONS["Register"]:
                self.user_manager.register_user()
            elif option == self.MENU_OPTIONS["Exit"]:
                print("Exiting...")
                exit()
            else:
                print("Invalid menu option.")
    
    def aws_main_menu(self, session):
        REGION = "eu-west-1" # TODO - should this be user input ???
        ec2_service = EC2(session, REGION)  # Initialize EC2 with AWS session
        while True:
            print("\nAWS Main Menu")
            print("1. EC2 Instances")
            print("2. Back to Main Menu")
            choice = read_range_integer("Select from menu: ", 1, 2)
            if choice == 1:
                self.ec2_menu(ec2_service)
            elif choice == 2:
                break

    def ec2_menu(self, ec2_service):
        while True:
            print("\nEC2 Instance Menu")
            print("1. List All Instances")
            print("2. Start Instance")
            print("3. Stop Instance")
            print("4. Create AMI")
            print("5. Delete AMI")
            print("6. Back")
            choice = read_range_integer("Select from menu: ", 1, 6)
            
            if choice == 1:
                ec2_service.list_instances()
            elif choice == 2:
                ec2_service.start_instance()
            elif choice == 3:
                ec2_service.stop_instance()
            elif choice == 4:
                ec2_service.create_ami()
            elif choice == 5:
                ec2_service.delete_ami()
            elif choice == 6:
                break
            else:
                print("Invalid option.")

def main():
    user_manager = UserManager()
    app = App(user_manager)
    app.handle_menu()

if __name__ == "__main__":
    main()
