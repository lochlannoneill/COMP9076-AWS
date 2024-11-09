from src.utils.reading_from_user import read_range_integer

class awsMenu:
    MENU_OPTIONS = {
        "EC2 Instances": 1,
        "Back": 2
    }
    
    def display(self):
        print("\nAWS Main Menu")
        for option, number in self.MENU_OPTIONS.items():
            print(f"{number}. {option}")

    def handle(self, ec2_service, ec2_menu):
        while True:
            self.display()
            
            choice = read_range_integer(
                "Select from menu: ",
                min(self.MENU_OPTIONS.values()),
                max(self.MENU_OPTIONS.values())
            )
            
            if choice == self.MENU_OPTIONS["EC2 Instances"]:
                return ec2_menu.handle(ec2_service)
            elif choice == self.MENU_OPTIONS["Back"]:
                return False
            else:
                print("Invalid option.")
                return False
