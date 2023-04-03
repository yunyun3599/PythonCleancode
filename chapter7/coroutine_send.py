import logging
logger = logging.getLogger("coroutine")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def yield_n_nums(start, n):
    values = None
    base = start
    prev_num = n
    try:
        while True:
            num = yield values
            if num is None:
                num = prev_num
            prev_num = num
            base += n
            values = [i for i in range(base, base + num)]
    except GeneratorExit:
        print("stop generating numbers")


if __name__ == "__main__":
    generator = yield_n_nums(0, 10)
    print(next(generator))
    print(next(generator))
    generator.send(3)
    print(next(generator))
    generator.send(5)
    print(next(generator))
    generator.close()
