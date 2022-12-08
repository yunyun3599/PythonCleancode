def check_remain_capacity(file_system, file_size):
    if file_system.total_size >= file_size:
        file_system.decrease_total_size(file_size)
        print("##### DOWNLOAD success #####")
        print(f"downloaded file size: {file_size}")
        print(f"remain file system: {file_system.total_size}")
        return True
    return False


def print_error_log(file_system, file_size):
    print("##### DOWNLOAD failed #####")
    print("lack of file system capacity")
    print(f"remain file system: {file_system.total_size}, download file size: {file_size}")


class FileSystem:
    def __init__(self, total_size: int):
        self.total_size = total_size

    def decrease_total_size(self, size: int):
        self.total_size = self.total_size - size


class FileDownloader:
    def __init__(self, file_system: FileSystem, file_size: int):
        self.file_system = file_system
        self.file_size = file_size

    def __enter__(self):
        return check_remain_capacity(self.file_system, self.file_size)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print_error_log(self.file_system, self.file_size)
        print("##########end#############\n")


class LackOfCapacityException(Exception):
    pass


if __name__ == "__main__":
    fs = FileSystem(100)
    download_list = [10, 20, 50, 30]

    for file in download_list:
        with FileDownloader(fs, file) as success:
            if success:
                print("Do something with downloaded file")
            else:
                raise LackOfCapacityException
