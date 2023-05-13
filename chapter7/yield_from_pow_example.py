def all_powers(n, pow):
    # 반복문을 사용해서 제곱 지수 하나씩 yield
    for i in range(pow + 1):
        yield n ** i


def yield_from_all_powers(n, pow):
    # yield from을 이용해 제곱 지수를 반환하는 제너레이터의 반환값을 모아 반환
    yield from (n ** i for i in range(pow + 1))


if __name__ == "__main__":
    print([result for result in all_powers(2, 3)])
    print(list(yield_from_all_powers(2, 3)))
