def func(param: dict):
    print(param)


# 가변 인자를 사용한 함수
def variadic_func(**elements):
    print(elements)


if __name__ == "__main__":
    dictionary = {'a': 'A', 'b': 'B', 'c': 'C'}

    # 언패킹
    func(dictionary)
    # func(**dictionary)

    # variadic_func(dictionary)
    variadic_func(**dictionary)
    variadic_func(dictionary=dictionary)
    variadic_func(key1="value1", key2="value2", key3="value3")

