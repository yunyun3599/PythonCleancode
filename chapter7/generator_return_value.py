def generator():
    yield 1
    yield 2
    return 3


if __name__ == "__main__":
    gen = generator()
    print(next(gen))
    print(next(gen))
    try:
        print(next(gen))
    except StopIteration as e:
        print(f"returned value: {e.value}")     # returned value: 3
