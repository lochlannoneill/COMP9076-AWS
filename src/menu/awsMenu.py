from src.utils.reading_from_user import read_range_integer
from src.menu.ec2Menu import ec2Menu
from src.menu.ebsMenu import ebsMenu
from src.models.ebs import EBSController
from src.models.ec2 import EC2Controller

class awsMenu:
    def __init__(self):
        self.ec2_menu = ec2Menu()
        self.ebs_menu = ebsMenu()
        self.options = {
            "EC2 Instances": 1,
            "EBS Storage": 2,
            "S3 Storage": 3,
            "Monitoring": 4,
            "Back": 5
        }

    def _display(self):
        print("\nAWS Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, session):
        # EC2
        ec2_controller = EC2Controller(
            session.get_ec2_resource(),
            session._create_client("ec2")
        )  # TODO - performance -> maybe just get resource here, and client after choice
        
        # EBS
        ebs = EBSController(
            session._create_client("ec2"),
            session.get_ec2_resource()
        )  # TODO - performance ->maybe just get resource here, and client after choice
        
        while True:
            self._display()
            choice = read_range_integer(
                "Select from menu: ",
                min(self.options.values()),
                max(self.options.values())
            )
            
            # EC2 Instances
            if choice == self.options["EC2 Instances"]:
                self.ec2_menu.handle(ec2_controller)
                
            # EBS Storage
            if choice == self.options["EBS Storage"]:
                self.ebs_menu.handle(ebs)
                
            # S3 Storage
            if choice == self.options["S3 Storage"]:
                pass  # TODO
            
            # Monitoring
            if choice == self.options["Monitoring"]:
                pass  # TODO
            
            # Back
            if choice == self.options["Back"]:
                return False
