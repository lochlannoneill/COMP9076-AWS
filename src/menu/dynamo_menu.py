from src.utils.reading_from_user import read_range_integer

class DynamoDBMenu:
    def __init__(self):
        self.options = {
            "Create Table": 1,
            "Get Item": 2,
            "Add Item": 3,
            "Delete Item": 4,
            "Back": 5
        }
    
    def _display(self):
        print("\nDynamoDB Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))
            
            # Get Item
            if choice == self.options["Get Item"]:
                service.get_item()
            
            # Create Table
            if choice == self.options["Create Table"]:
                service.create_table()
                
            # Add Item
            elif choice == self.options["Add Item"]:
                service.add_item()
                
            # Delete Item
            elif choice == self.options["Delete Item"]:
                service.delete_item()
                
            # Back
            elif choice == self.options["Back"]:
                return False