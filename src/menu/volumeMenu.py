from src.utils.reading_from_user import read_range_integer

class volumeMenu:
    def __init__(self):
        self.options = {
            "List Volumes": 1,
            "Create Volume": 2,
            "Create Volume From Snapshot": 3,
            "Attach Volume": 4,
            "Detach Volume": 5,
            "Modify Volume": 6,
            "Delete Volume": 7,
            "List Snapshots": 8,
            "Create Snapshot": 9,
            "Delete Snapshot": 10,
            "Back": 11
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

            if choice == self.options["List Volumes"]:
                ec2_service.list_volumes()
            elif choice == self.options["Create Volume"]:
                ec2_service.create_volume()
            elif choice == self.options["Create Volume From Snapshot"]:
                ec2_service.create_volume_from_snapshot()
            elif choice == self.options["Attach Volume"]:
                ec2_service.attach_volume()
            elif choice == self.options["Detach Volume"]:
                ec2_service.detach_volume()
            elif choice == self.options["Modify Volume"]:
                ec2_service.modify_volume()
            elif choice == self.options["Delete Volume"]:
                ec2_service.delete_volume()
            elif choice == self.options["Snapshot Volume"]:
                ec2_service.snapshot_volume()
            elif choice == self.options["List Snapshots"]:
                ec2_service.list_snapshots()
            elif choice == self.options["Create Snapshot"]:
                ec2_service.create_snapshot()
            elif choice == self.options["Delete Snapshot"]:
                ec2_service.delete_snapshot()
            elif choice == self.options["Back"]:
                return False
