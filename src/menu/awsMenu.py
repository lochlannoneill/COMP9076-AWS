from src.utils.reading_from_user import read_range_integer
from src.models.resource import Resource
from src.models.ebs import EBSController
from src.models.ec2 import EC2Controller
from src.models.s3 import S3Controller
from src.menu.ec2Menu import ec2Menu
from src.menu.ebsMenu import ebsMenu
from src.menu.s3Menu import s3Menu

class awsMenu:
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
                ec2Menu().handle(EC2Controller(self.res.EC2Resource()))
                
            # EBS Storage
            if choice == self.options["EBS Storage"]:
                ebsMenu().handle(EBSController(self.res.EC2Resource()))
                
            # S3 Storage
            if choice == self.options["S3 Storage"]:
                s3Menu().handle(S3Controller(res.S3Resource()))
            
            # Monitoring
            if choice == self.options["Monitoring"]:
                pass
            
            # Back
            if choice == self.options["Back"]:
                return False
