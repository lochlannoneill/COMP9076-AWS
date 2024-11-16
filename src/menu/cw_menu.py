from src.utils.reading_from_user import read_range_integer

class CWMenu:
    def __init__(self):
        self.options = {
            "List Metrics": 1,
            "Get Metric Statistics": 2,
            "Set Alarm": 3,
            "Delete Alarm": 4,
            "Free Tier AWS Services": 5,
            "Back": 6
        }
    
    def _display(self):
        print("\nCloudWatch Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))
            
            # List Metrics
            if choice == self.options["List Metrics"]:
                service.list_metrics()
            
            # Get Metric Statistics
            if choice == self.options["Get Metric Statistics"]:
                service.get_metric_statistics()
            
            # Set Alarm
            if choice == self.options["Set Alarm"]:
                service.set_alarm()
            
            # Delete Alarm
            if choice == self.options["Delete Alarm"]:
                service.delete_alarm()
            
            # Free Tier AWS Services
            if choice == self.options["Free Tier AWS Services"]:
                service.free_tier_aws_services()
            
            # Back
            if choice == self.options["Back"]:
                return False
