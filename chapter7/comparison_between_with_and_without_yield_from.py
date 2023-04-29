def generator(*iterables):
    for iterable in iterables:
        for value in iterable:
            yield value


def yield_from_generator(*iterables):
    for iterable in iterables:
        yield from iterable


if __name__ == "__main__":
    iterable_list = ['abc', 'ABC', '123', 'xyz']

    val_list = []
    # yield from 사용 없이 중첩 구문 사용
    for val in generator(*iterable_list):
        val_list.append(val)
    print(val_list)

    # yield from 사용
    val_list2 = list(yield_from_generator(*iterable_list))
    print(val_list2)
