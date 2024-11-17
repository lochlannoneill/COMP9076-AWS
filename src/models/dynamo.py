from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string, read_nonnegative_float

class DynamoDBController:
    def __init__(self, client):
        """Initialize with a boto3 session."""
        self.client = client

    # COMPLETED
    def list_tables(self):
        """List all tables in DynamoDB."""
        try:
            response = self.client.list_tables()
            tables = response.get('TableNames', [])
            
            print("\nTables in DynamoDB:")
            if not tables:
                print("No tables found.")
            else:
                for table in tables:
                    print(f"\t{table}")
                    
        except Exception as e:
            print(e)
            
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
    def delete_table(self):
        """Delete a table in DynamoDB."""
        table_name = read_nonempty_string("\nEnter table name to delete: ")
        
        try:
            # Delete the table from DynamoDB
            response = self.client.delete_table(
                TableName=table_name
            )
            print(f"Deleted '{table_name}'")
            
        except Exception as e:
            print(e)

    # COMPLETED
    def list_items_in_table(self):
        """Retrieve all items from a table in DynamoDB."""
        table_name = read_nonempty_string("\nEnter table name: ")
        try:
            response = self.client.scan(
                TableName=table_name
            )
            items = response.get('Items', [])
            
            print(f"\nItems in '{table_name}': ")
            if not items:
                print(f"No items found in table '{table_name}'.")
            else:
                for item in items:
                    print(f"{item}")
                
        except Exception as e:
            print(e)
            
    # TODO
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
            attribute = read_nonempty_string(f"\nEnter attribute {i+1} name: ")
            data = read_nonempty_string(f"Enter data for {attribute}: ")
            item_data[attribute] = {'S': data}  # Assuming the data is a string ('S')

        try:
            # Add the item to DynamoDB
            response = self.client.put_item(
                TableName=table_name,
                Item=item_data
            )
            print(f"\nAdded item '{item_id}' to '{table_name}'")
            
        except Exception as e:
            print(e)
        
    # COMPLETED  
    def delete_item(self):
        """Delete an item from a table in DynamoDB."""
        table_name = read_nonempty_string("\nEnter table name to delete item: ")
        item_id = read_nonempty_string("Enter item ID to delete: ")
        try:
            response = self.client.delete_item(
                TableName=table_name,
                Key={
                    'id': {'S': item_id}
                }
            )
            print(f"Deleted item '{item_id}' from '{table_name}'")
            
        except Exception as e:
            print(e)