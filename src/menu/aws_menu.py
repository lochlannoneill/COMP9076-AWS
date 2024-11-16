from src.models.resource import Resource
from src.menu.ec2_menu import EC2Menu
from src.models.ec2 import EC2Controller
from src.menu.ebs_menu import EBSMenu
from src.models.ebs import EBSController
from src.menu.s3_menu import S3Menu
from src.models.s3 import S3Controller
from src.utils.reading_from_user import read_range_integer

class AWSMenu:
    def __init__(self, user_credentials):
        self.res = Resource(user_credentials)
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

    def handle(self):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))
            
            # EC2 Instances
            if choice == self.options["EC2 Instances"]:
                ec2 = EC2Controller(self.res.EC2Resource())
                EC2Menu().handle(ec2)
            
            # EBS Storage
            if choice == self.options["EBS Storage"]:
                ebs = EBSController(self.res.EC2Resource())  # EBS is part of EC2
                EBSMenu().handle(ebs)
            
            # S3 Storage
            if choice == self.options["S3 Storage"]:
                s3 = S3Controller(self.res.S3Resource())
                S3Menu().handle(s3)
            
            # Monitoring
            if choice == self.options["Monitoring"]:
                pass
            
            # Back
            if choice == self.options["Back"]:
                return False
