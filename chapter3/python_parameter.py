def func(immutable: str, mutable: list, mutable_dict: dict):
    appended_str = " appended str"
    immutable += appended_str
    mutable += appended_str
    mutable_dict.update(c='C')


if __name__ == "__main__":
    base_string = "base string"
    base_list = list(base_string)
    base_dict = dict({'a': 'A', 'b': 'B'})

    func(base_string, base_list, base_dict)
    print("immutable_result:", base_string)
    print("mutable_result:", base_list)
    print("mutable_dict_result:", base_dict)
