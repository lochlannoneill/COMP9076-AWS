from src.utils.reading_from_user import read_range_integer

class ec2Menu:
    def __init__(self):
        self.options = {
            "List All Instances": 1,
            "Start Instance": 2,
            "Stop Instance": 3,
            "Create AMI": 4,
            "Delete AMI": 5,
            "Back": 6
        }
    
    def _display(self):
        print("\nAWS Main Menu")
        for option, number in self.options.items():
            print(f"{number}. {option}")

    def handle(self, ec2_service):
        while True:
            self._display()
            choice = read_range_integer(
                "Select from menu: ",
                min(self.options.values()),
                max(self.options.values())
            )

            if choice == self.options["List All Instances"]:
                ec2_service.list_instances()
            elif choice == self.options["Start Instance"]:
                ec2_service.start_instance()
            elif choice == self.options["Stop Instance"]:
                ec2_service.stop_instance()
            elif choice == self.options["Create AMI"]:
                ec2_service.create_ami()
            elif choice == self.options["Delete AMI"]:
                ec2_service.delete_ami()
            elif choice == self.options["Back"]:
                return False
