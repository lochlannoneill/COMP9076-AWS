from src.utils.reading_from_user import read_range_integer

class S3Menu:
    def __init__(self):
        self.options = {
            "List Buckets": 1,
            "Delete Bucket": 2,
            "List Objects in Bucket": 3,
            "Upload Object": 4,
            "Download Object": 5,
            "Delete Object": 6,
            "Back": 7
        }
    
    def _display(self):
        print("\nS3 Storage Menu")
        for option, number in self.options.items():
            print(f"\t{number}. {option}")

    def handle(self, service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))

            # List Buckets
            if choice == self.options["List Buckets"]:
                service.list_buckets()
            
            # Delete Bucket
            elif choice == self.options["Delete Bucket"]:
                service.delete_bucket()
            
            # List Objects in Bucket
            elif choice == self.options["List Objects in Bucket"]:
                service.list_objects()
            
            # Upload Object
            elif choice == self.options["Upload Object"]:
                service.upload_object()
            
            # Download Object
            elif choice == self.options["Download Object"]:
                service.download_object()
            
            # Delete Object
            elif choice == self.options["Delete Object"]:
                service.delete_object()
            
            # Back
            elif choice == self.options["Back"]:
                return False
