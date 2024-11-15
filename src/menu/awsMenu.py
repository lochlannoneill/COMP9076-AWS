from src.utils.reading_from_user import read_range_integer
from src.menu.ec2Menu import ec2Menu
from src.menu.ebsMenu import ebsMenu
from src.menu.s3Menu import s3Menu
from src.models.ebs import EBSController
from src.models.ec2 import EC2Controller
from src.models.s3 import S3Controller

class awsMenu:
    def __init__(self, resource):
        self.ec2 = EC2Controller(resource.get_ec2_resource())
        self.ebs = EBSController(resource.get_ec2_resource())
        self.s3 = S3Controller(resource.get_s3_resource())
        # self.cloudwatch_client = resource.get_cloudwatch_client()  # Example of using a client
        
        self.ec2_menu = ec2Menu()
        self.ebs_menu = ebsMenu()
        self.s3_menu = s3Menu()
        
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
                self.ec2_menu.handle(self.ec2)
                
            # EBS Storage
            if choice == self.options["EBS Storage"]:
                self.ebs_menu.handle(self.ebs)
                
            # S3 Storage
            if choice == self.options["S3 Storage"]:
                self.s3_menu.handle(self.s3)
            
            # Monitoring
            if choice == self.options["Monitoring"]:
                pass
            
            # Back
            if choice == self.options["Back"]:
                return False
