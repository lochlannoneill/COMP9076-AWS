from src.utils.reading_from_user import read_range_integer

class ec2Menu:
    MENU_OPTIONS = {
        "List All Instances": 1,
        "Start Instance": 2,
        "Stop Instance": 3,
        "Create AMI": 4,
        "Delete AMI": 5,
        "Back": 6
    }
    
    def display(self):
        print("\nEC2 Instance Menu")
        for option, number in self.MENU_OPTIONS.items():
            print(f"{number}. {option}")

    def handle(self, ec2_service):
        while True:
            self.display()
            choice = read_range_integer(
                "Select from menu: ",
                min(self.MENU_OPTIONS.values()),
                max(self.MENU_OPTIONS.values())
            )

            if choice == self.MENU_OPTIONS["List All Instances"]:
                ec2_service.list_instances()
            elif choice == self.MENU_OPTIONS["Start Instance"]:
                ec2_service.start_instance()
            elif choice == self.MENU_OPTIONS["Stop Instance"]:
                ec2_service.stop_instance()
            elif choice == self.MENU_OPTIONS["Create AMI"]:
                ec2_service.create_ami()
            elif choice == self.MENU_OPTIONS["Delete AMI"]:
                ec2_service.delete_ami()
            elif choice == self.MENU_OPTIONS["Back"]:
                return False
            else:
                print("Invalid menu choice.")
            return True
