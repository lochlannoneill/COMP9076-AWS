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
            read_capacity_units = 5
            write_capacity_units = 5

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
                    "ReadCapacityUnits": read_capacity_units,
                    "WriteCapacityUnits": write_capacity_units
                }
            )
            print(f"Created table '{table_name}'")
        
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
            print(f"Error retrieving item: {e}")
        
    # TODO
    def add_item(self):
        print("Not Implemented Yet")
        
    # TODO  
    def delete_item(self):
        print("Not Implemented Yet")
    