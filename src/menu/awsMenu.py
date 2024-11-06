from src.utils.reading_from_user import read_range_integer

class awsMenu:
    def display(self):
        print("\nAWS Main Menu")
        print("1. EC2 Instances")
        print("2. Back to Main Menu")

    def handle(self, ec2_service):
        if choice == 1:
            return True
        elif choice == 2:
            return False
        else:
            print("Invalid option.")
            return False
            choice = read_range_integer("Select from menu: ", 1, 2)
