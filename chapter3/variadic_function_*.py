def func(one, two, three):
    print(one)
    print(two)
    print(three)


# 가변 인자를 사용한 함수
def variadic_func(*elements):
    for element in elements:
        print(element)


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]

    # 언패킹
    one, two, three, four, five = lst
    print(one, two, three, four, five)
    func(one, two, three)

    # 부분적인 언패킹
    one, two, three, *last = lst
    print(*last)
    print(last)

    variadic_func(one, two, three, four, five)
    variadic_func(last)
    variadic_func(*last)

