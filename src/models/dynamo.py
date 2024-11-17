from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string, read_nonnegative_float

class DynamoDBController:
    def __init__(self, client):
        """Initialize with a boto3 session."""
        self.client = client

    # COMPLETED
    def create_table(self):
        """Create a table in DynamoDB."""
        try:
            table_name = read_nonempty_string("\nEnter table name: ")
            primary_key = read_nonempty_string("Enter primary key: ")

            response = self.client.create_table(
                TableName=table_name,
                KeySchema=[
                    {
                        "AttributeName": primary_key,
                        "KeyType": "HASH"
                    }
                ],
                AttributeDefinitions=[
                    {
                        "AttributeName": primary_key,
                        "AttributeType": "S"
                    }
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 5,
                    "WriteCapacityUnits": 5
                }
            )
            print(f"Created table '{table_name}'")
        
        except Exception as e:
            print(e)
        
    # COMPLETED
    def get_items_in_table(self):
        """Retrieve all items from a table in DynamoDB."""
        table_name = read_nonempty_string("\nEnter table name: ")
        try:
            response = self.client.scan(
                TableName=table_name
            )
            items = response.get('Items', [])
            
            print("Retrieved items: ")
            if not items:
                print(f"No items found in table '{table_name}'.")
            else:
                for item in items:
                    print(f"{item}")
                
        except Exception as e:
            print(e)
            
    # COMPLETED
    def get_item(self):
        """Retrieve an item from a table in Dynamo"""
        table_name = read_nonempty_string("\nEnter table name: ")
        item_id = read_nonempty_string("Enter item ID: ")
        try:
            response = self.client.get_item(
                TableName=table_name,
                Key={
                    'ID': {'S': item_id}
                }
            )
            item = response.get('Item', {})
            if not item:
                print(f"No item found with ID '{item_id}'.")
            else:
                print(f"Retrieved item: {item}")
                
        except Exception as e:
            print(e)
            
    # COMPLETED
    def add_item(self):
        """Add an item to a table in DynamoDB with user-defined headings."""
        table_name = read_nonempty_string("\nEnter table name to add item: ")
        item_id = read_nonempty_string("Enter item ID: ")
        num_headings = read_nonnegative_integer("Enter the number of headings (attributes) you want to add: ")
        
        # Dictionary to hold the attributes for the item
        item_data = {'id': {'S': item_id}}  # Assuming the ID is a string ('S')

        # Loop to collect the headings and their corresponding data
        for i in range(num_headings):
            heading = read_nonempty_string(f"\nEnter heading {i+1} (attribute name): ")
            data = read_nonempty_string(f"Enter data for {heading}: ")
            item_data[heading] = {'S': data}  # Assuming the data is a string ('S')

        try:
            # Add the item to DynamoDB
            response = self.client.put_item(
                TableName=table_name,
                Item=item_data
            )
            print(f"Added item '{item_id}' to '{table_name}'")
            
        except Exception as e:
            print(e)


        
    # TODO  
    def delete_item(self):
        print("Not Implemented Yet")
    