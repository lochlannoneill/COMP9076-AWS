from src.utils.reading_from_user import read_range_integer
from src.menu.ec2Menu import ec2Menu

class awsMenu:
    def __init__(self):
        self.ec2_menu = ec2Menu()
        self.options = {
            "EC2 Instances": 1,
            "EBS Volumes": 2,
            "S3 Buckets": 3,
            "Monitoring": 4,
            "Back": 5
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
            
            if choice == self.options["EC2 Instances"]:
                self.ec2_menu.handle(ec2_service)
            if choice == self.options["EBS Volumes"]:
                pass  # TODO
            if choice == self.options["S3 Buckets"]:
                pass  # TODO
            if choice == self.options["Monitoring"]:
                pass  # TODO
            if choice == self.options["Back"]:
                return False
