if __name__ == "__main__":
    sample_list = list(range(1, 11))

    if sample_list[1:10:2] == sample_list[slice(1, 10, 2)]:
        print("sample_list[1:10:2] == sample_list[slice(1, 10, 2)] is True")
    else:
        print("sample_list[1:10:2] == sample_list[slice(1, 10, 2)] is False")
