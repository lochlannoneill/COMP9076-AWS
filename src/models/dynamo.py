from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string, read_nonnegative_float

class DynamoDBController:
    def __init__(self, client):
        """Initialize with a boto3 session."""
        self.client = client

    # COMPLETED
    def create_table(self):
        """Create a table in DynamoDB."""
        try:
            table_name = read_nonempty_string("Enter table name: ")
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
        
    # TODO
    def get_item(self):
        print("Not Implemented Yet")
        
    # TODO
    def add_item(self):
        print("Not Implemented Yet")
        
    # TODO  
    def delete_item(self):
        print("Not Implemented Yet")
    