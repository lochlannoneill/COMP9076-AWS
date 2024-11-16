from src.utils.reading_from_user import read_range_integer

class CWMenu:
    def __init__(self):
        self.options = {
            "List Metrics": 1,
            "Get Metric Data": 2,
            "Put Metric Data": 3,
            "Set Alarm": 4,
            "Delete Alarm": 5,
            "Free Tier AWS Services": 6,
            "Back": 7
        }
    
    def _display(self):
        print("\nCW Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))
            
            # List Metrics
            if choice == self.options["List Metrics"]:
                service.list_metrics()
            
            # Get Metric Data
            if choice == self.options["Get Metric Data"]:
                service.get_metric_data()
            
            # Put Metric Data
            if choice == self.options["Put Metric Data"]:
                service.put_metric_data()
            
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
