from src.utils.reading_from_user import read_range_integer
from src.menu.ec2Menu import ec2Menu

class awsMenu:
    def __init__(self):
        self.ec2_menu = ec2Menu()
        
    def _display(self):
        print("\nAWS Main Menu")
        print("1. EC2 Instances")
        print("2. Back to Main Menu")

    def handle(self, ec2_service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, 2)
            if choice == 1:
                self.ec2_menu.handle(ec2_service)
            elif choice == 2:
                return False
            else:
                print("Invalid option.")
                return False
