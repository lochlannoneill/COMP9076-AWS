from src.utils.reading_from_user import read_range_integer

class volumeMenu:
    def __init__(self):
        self.options = {
            "List All Volumes": 1,
            "Create New Volume": 2,
            "Attach Volume To Instance": 3,
            "Detach Volume To Instance": 4,
            "Modify Volume": 5,
            "Snapshot Volume": 6,
            "Create Volume From Snapshot": 7,
            "Delete Available Volume": 8,
            "Back": 9
        }
    
    def _display(self):
        print("\nVolume Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, ec2_service):
        while True:
            self._display()
            choice = read_range_integer(
                "Select from menu: ",
                min(self.options.values()),
                max(self.options.values())
            )

            if choice == self.options["List All Volumes"]:
                ec2_service.list_volumes()
            elif choice == self.options["Create New Volume"]:
                ec2_service.create_volume()
            elif choice == self.options["Attach Volume To Instance"]:
                ec2_service.attach_volume()
            elif choice == self.options["Detach Volume To Instance"]:
                ec2_service.detach_volume()
            elif choice == self.options["Modify Volume"]:
                ec2_service.modify_volume()
            elif choice == self.options["Snapshot Volume"]:
                ec2_service.snapshot_volume()
            elif choice == self.options["Create Volume From Snapshot"]:
                ec2_service.create_volume_from_snapshot()
            elif choice == self.options["Delete Available Volume"]:
                ec2_service.delete_volume()
            elif choice == self.options["Back"]:
                return False
