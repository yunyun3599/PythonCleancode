def search_nested_bad(array, target):
    location = None
    for i, row in enumerate(array):
        for j, value in enumerate(row):
            if value == target:
                location = (i, j)
                break
        if location:
            break
    if not location:
        raise ValueError(f"{target} not found")
    return location


def search_nested_good(array, target):
    try:
        location = next(location for location, value in _iterate_array2d(array) if value == target)
    except StopIteration:
        raise ValueError(f"target not found")
    return location


def _iterate_array2d(array2d):
    for i, row in enumerate(array2d):
        for j, value in enumerate(row):
            yield (i, j), value


if __name__ == "__main__":
    map2d = [[i * j for i in range(1, 6)] for j in range(1, 6)]
    print(search_nested_bad(map2d, 9))
    print(search_nested_good(map2d, 9))
