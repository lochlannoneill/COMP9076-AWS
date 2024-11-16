from src.utils.reading_from_user import read_range_integer

class EBSMenu:
    def __init__(self):
        self.options = {
            "List Volumes": 1,
            "Create Volume": 2,
            "Attach Volume": 3,
            "Detach Volume": 4,
            "Modify Volume": 5,
            "Delete Volume": 6,
            "List Snapshots": 7,
            "Create Snapshot": 8,
            "Delete Snapshot": 9,
            "Create Volume From Snapshot": 10,
            "Back": 11
        }
    
    def _display(self):
        print("\nEBS Storage Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))

            # List Volumes
            if choice == self.options["List Volumes"]:
                service.list_volumes()
            
            # Create Volume
            elif choice == self.options["Create Volume"]:
                service.create_volume()
            
            # Attach Volume
            elif choice == self.options["Attach Volume"]:
                service.attach_volume()
            
            # Detach Volume
            elif choice == self.options["Detach Volume"]:
                service.detach_volume()
            
            # Modify Volume
            elif choice == self.options["Modify Volume"]:
                service.modify_volume()
            
            # Delete Volume
            elif choice == self.options["Delete Volume"]:
                service.delete_volume()
            
            # List Snapshots
            elif choice == self.options["List Snapshots"]:
                service.list_snapshots()
            
            # Create Snapshot
            elif choice == self.options["Create Snapshot"]:
                service.create_snapshot()
            
            # Delete Snapshot
            elif choice == self.options["Delete Snapshot"]:
                service.delete_snapshot()
            
            # Create Volume From Snapshot
            elif choice == self.options["Create Volume From Snapshot"]:
                service.create_volume_from_snapshot()
            
            # Back
            elif choice == self.options["Back"]:
                return False
