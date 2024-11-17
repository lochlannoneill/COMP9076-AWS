from src.utils.reading_from_user import read_range_integer

class CWMenu:
    def __init__(self):
        self.options = {
            "Get Metric Statistics": 1,
            "List Alarms": 2,
            "Set Alarm": 3,
            "Delete Alarm": 4,
            "Back": 5
        }
    
    def _display(self):
        print("\nCloudWatch Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))
            
            # Get Metric Statistics
            if choice == self.options["Get Metric Statistics"]:
                service.get_metric_statistics()
                
            # List Alarms
            if choice == self.options["List Alarms"]:
                service.list_alarms()
            
            # Set Alarm
            if choice == self.options["Set Alarm"]:
                service.set_alarm()
            
            # Delete Alarm
            if choice == self.options["Delete Alarm"]:
                service.delete_alarm()
            
            # Back
            if choice == self.options["Back"]:
                return False
