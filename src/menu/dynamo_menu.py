from src.utils.reading_from_user import read_range_integer

class DynamoDBMenu:
    def __init__(self):
        self.options = {
            "Create Table": 1,
            "Get All Items in Table": 2,
            "Get Item": 3,
            "Add Item": 4,
            "Delete Item": 5,
            "Back": 6
        }
    
    def _display(self):
        print("\nDynamoDB Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))
            
            # Create Table
            if choice == self.options["Create Table"]:
                service.create_table()
            
            # Get All Items in Table
            elif choice == self.options["Get All Items in Table"]:
                service.get_items_in_table()
            
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