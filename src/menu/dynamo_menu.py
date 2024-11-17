from src.utils.reading_from_user import read_range_integer

class DynamoDBMenu:
    def __init__(self):
        self.options = {
            "List Tables": 1,
            "Create Table": 2,
            "List Items In Table": 3,
            "Get Item": 4,
            "Add Item": 5,
            "Delete Item": 6,
            "Back": 7
        }
    
    def _display(self):
        print("\nDynamoDB Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))
            
            # List Tables
            if choice == self.options["List Tables"]:
                service.list_tables()
            
            # Create Table
            if choice == self.options["Create Table"]:
                service.create_table()
            
            # List Items In Table
            elif choice == self.options["List Items In Table"]:
                service.list_items_in_table()
            
            # Get Item
            elif choice == self.options["Get Item"]:
                service.get_item()
            
            # Add Item
            elif choice == self.options["Add Item"]:
                service.add_item()
                
            # Delete Item
            elif choice == self.options["Delete Item"]:
                service.delete_item()
                
            # Back
            elif choice == self.options["Back"]:
                return False