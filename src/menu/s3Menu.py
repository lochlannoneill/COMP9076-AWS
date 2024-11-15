from src.utils.reading_from_user import read_range_integer

class s3Menu:
    def __init__(self):
        self.options = {
            "List Buckets": 1,
            # "Create Bucket": 2,
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

    def handle(self, s3_service):
        while True:
            self._display()
            choice = read_range_integer("Select from menu: ", 1, len(self.options))

            if choice == self.options["List Buckets"]:
                s3_service.list_buckets()
            # TODO: Implement create_bucket
            # elif choice == self.options["Create Bucket"]:
            #     s3_service.create_bucket()
            elif choice == self.options["Delete Bucket"]:
                s3_service.delete_bucket()
            elif choice == self.options["List Objects in Bucket"]:
                s3_service.list_objects()
            elif choice == self.options["Upload Object"]:
                s3_service.upload_object()
            elif choice == self.options["Download Object"]:
                s3_service.download_object()
            elif choice == self.options["Delete Object"]:
                s3_service.delete_object()
            elif choice == self.options["Back"]:
                return False
