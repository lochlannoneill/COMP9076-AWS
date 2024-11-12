from src.utils.reading_from_user import read_range_integer

class ec2Menu:
    def _display(self):
        print("\nAWS Main Menu")
        MENU_OPTIONS = {
            "List All Instances": 1,
            "Start Instance": 2,
            "Stop Instance": 3,
            "Create AMI": 4,
            "Delete AMI": 5,
            "Back": 6
        }
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
                return False
            else:
                print("Invalid option.")
