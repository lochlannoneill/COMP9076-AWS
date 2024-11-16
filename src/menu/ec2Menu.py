from src.utils.reading_from_user import read_range_integer

class EC2Menu:
    def __init__(self):
        self.options = {
            "List All Instances": 1,
            # "Create Instance": 2,
            "Start Instance": 2,
            "Stop Instance": 3,
            "Delete Instance": 4,
            "List AMIs of Instance": 5,
            "Create AMI": 6,
            "Delete AMI": 7,
            "Back": 8
        }
    
    def _display(self):
        print("\nEC2 Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, ec2_service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))

            if choice == self.options["List All Instances"]:
                ec2_service.list_instances()
            # TODO - Implement create_instance
            # elif choice == self.options["Create Instance"]:
                # ec2_service.create_instance()
            elif choice == self.options["Start Instance"]:
                ec2_service.start_instance()
            elif choice == self.options["Stop Instance"]:
                ec2_service.stop_instance()
            elif choice == self.options["Delete Instance"]:
                ec2_service.delete_instance()
            elif choice == self.options["List AMIs of Instance"]:
                ec2_service.list_amis()
            elif choice == self.options["Create AMI"]:
                ec2_service.create_ami()
            elif choice == self.options["Delete AMI"]:
                ec2_service.delete_ami()
            elif choice == self.options["Back"]:
                return False
