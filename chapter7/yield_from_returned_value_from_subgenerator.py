import logging

logger = logging.getLogger("yield_from_logger")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def sequence(name, start, end):
    logger.info(f"{name} 제너레이터 {start}에서 시작")
    # start에서 end-1까지 값을 하나씩 yield
    yield from range(start, end)
    logger.info(f"{name} 제너레이터 {end}에서 종료")
    return end


def collect_result():
    # 0~4까지 sequence에서 yield 받은 값을 하나씩 다신 yield
    # sequence에서 return 한 5가 step1의 값
    step1 = yield from sequence("first", 0, 5)
    # step1인 5부터 9까지 sequence에서 yield 받음
    # sequence에서 return한 10이 step2의 값
    step2 = yield from sequence("second", step1, 10)
    # 15를 리턴하고 stop
    return step1 + step2


if __name__ == "__main__":
    generator = collect_result()

    try:
        print(next(generator))
        print(next(generator))
        print(next(generator))
        print(next(generator))
        print(next(generator))
        print(next(generator))
        print(next(generator))
        print(next(generator))
        print(next(generator))
        print(next(generator))
        print(next(generator))
        # for문을 통해 제너레이터를 다음 값으로 이동시킨 경우 모든 값을 출력한 후에 next를 한번 더 불러도 리턴값이 나오지 않음 (왜?!?!)
        # for val in generator:
        #     print(val)
        # next(generator)
    except StopIteration as e:
        print(f"returned value: {e.value}")     # returned value: 15
