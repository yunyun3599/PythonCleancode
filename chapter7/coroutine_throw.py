import logging
logger = logging.getLogger("coroutine")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


class CustomException(Exception):
    pass


def yield_n_nums(start, n):
    base = start
    while True:
        try:
            yield [i for i in range(base, base + n)]
            base += n
        except CustomException as e:
            logger.info(f"에러 {e} 발생, 게속 진행")
        except Exception as e:
            logger.error("에러 발생, 종료")
            break


if __name__ == "__main__":
    generator = yield_n_nums(0, 10)
    print(next(generator))
    generator.throw(CustomException)
    print(next(generator))
    print(next(generator))
    generator.throw(RuntimeError)
    print(next(generator))
