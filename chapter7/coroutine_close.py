def yield_n_nums(start, n):
    base = start
    try:
        while True:
            yield [i for i in range(base, base + n)]
            base += n
    except GeneratorExit:
        print("stop generating numbers")


if __name__ == "__main__":
    generator = yield_n_nums(0, 10)
    print(next(generator))
    print(next(generator))
    generator.close()
