from utils.reading_from_user import read_range_integer

class mainMenu:
    MENU_OPTIONS = {
        "Login": 1,
        "Register": 2,
        "Exit": 3
    }

    def display(self):
        print("\nMain Menu")
        for option, number in self.MENU_OPTIONS.items():
            print(f"{number}. {option}")

    def handle(self, user_manager):
        while True:
            self.display()
            option = read_range_integer(
                "Select from menu: ",
                min(self.MENU_OPTIONS.values()),
                max(self.MENU_OPTIONS.values())
            )

            if option == self.MENU_OPTIONS["Login"]:
                return user_manager.login_user()
            elif option == self.MENU_OPTIONS["Register"]:
                user_manager.register_user()
            elif option == self.MENU_OPTIONS["Exit"]:
                print("Exiting...")
                exit()
            else:
                print("Invalid menu option.")


class awsMenu:
    def display(self):
        print("\nAWS Main Menu")
        print("1. EC2 Instances")
        print("2. Back to Main Menu")

    def handle(self, ec2_service):
        choice = read_range_integer("Select from menu: ", 1, 2)
        if choice == 1:
            return True
        elif choice == 2:
            return False
        else:
            print("Invalid option.")
            return False


class ec2Menu:
    def display(self):
        print("\nEC2 Instance Menu")
        print("1. List All Instances")
        print("2. Start Instance")
        print("3. Stop Instance")
        print("4. Create AMI")
        print("5. Delete AMI")
        print("6. Back")

    def handle(self, ec2_service):
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
        return True
