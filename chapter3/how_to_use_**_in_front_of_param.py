# **var (var는 dict형)
# dict.update(a='b') 형태 가능
# dict.update({'a': 'b'}) 는 dict.update(a='b')와 동일
def get_dict_param_test(original: dict, **it_is_dict):
    print(it_is_dict)
    original.update(**it_is_dict)
    original.update(d=4)


if __name__ == "__main__":
    origin_dict = {'a': {'a': 1}}
    get_dict_param_test(origin_dict, b=2, c=3)
    print(origin_dict)
