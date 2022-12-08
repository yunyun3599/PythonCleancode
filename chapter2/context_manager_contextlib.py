import contextlib
from context_manager import FileSystem, LackOfCapacityException, check_remain_capacity, print_error_log


@contextlib.contextmanager
def file_downloader(file_system, file_size):
    result = check_remain_capacity(file_system, file_size)
    try:
        yield result
    except LackOfCapacityException:
        print_error_log(file_system, file_size)
    print("##########end#############\n")


if __name__ == "__main__":
    fs = FileSystem(100)
    download_list = [10, 20, 50, 30]
    
    for file in download_list:
        with file_downloader(fs, file) as success:
            if success:
                print("Do something with downloaded file")
            else:
                raise LackOfCapacityException
