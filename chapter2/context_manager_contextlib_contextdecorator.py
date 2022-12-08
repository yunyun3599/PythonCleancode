import contextlib
from context_manager import FileSystem, LackOfCapacityException, check_remain_capacity, print_error_log


class file_downloader_decorator(contextlib.ContextDecorator):
    def __init__(self, file_system, file_size):
        self.file_system = file_system
        self.file_size = file_size

    def __enter__(self):
        return check_remain_capacity(self.file_system, self.file_size)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print_error_log(self.file_system, self.file_size)
        print("##########end#############\n")


if __name__ == "__main__":
    fs = FileSystem(100)
    download_list = [10, 20, 50, 30]

    for file in download_list:
        @file_downloader_decorator(fs, file)
        def download_files():
            print("Do something with downloaded file")

        download_files()

