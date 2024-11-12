from src.utils.reading_from_user import read_range_integer

class ec2Menu:
    def _display(self):
        print("\nEC2 Instance Menu")
        print("1. List All Instances")
        print("2. Start Instance")
        print("3. Stop Instance")
        print("4. Create AMI")
        print("5. Delete AMI")
        print("6. Back")

    def handle(self, ec2_service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, 6)

            if choice == 1:
                ec2_service.list_instances()
            elif choice == 2:
                ec2_service.start_instance()
            elif choice == 3:
                ec2_service.stop_instance()
            elif choice == 4:
                ec2_service.create_ami()
            elif choice == 5:
                ec2_service.delete_ami()
            elif choice == 6:
                return False
            else:
                print("Invalid option.")
