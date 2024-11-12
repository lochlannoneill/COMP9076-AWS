from src.utils.reading_from_user import read_range_integer
from src.menu.ec2Menu import ec2Menu

class awsMenu:
    MENU_OPTIONS = {
        "EC2 Instances": 1,
        "Back": 2
    }
    
    def __init__(self):
        self.ec2_menu = ec2Menu()
        
    def _display(self):
        print("\nAWS Main Menu")
        for option, number in self.MENU_OPTIONS.items():
            print(f"{number}. {option}")

    def handle(self, ec2_service):
        while True:
            self._display()
            
            choice = read_range_integer(
                "Select from menu: ",
                min(self.MENU_OPTIONS.values()),
                max(self.MENU_OPTIONS.values())
            )
            
            if choice == 1:
                self.ec2_menu.handle(ec2_service)
            elif choice == 2:
                return False
            else:
                print("Invalid option.")
                return False
