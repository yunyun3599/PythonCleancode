import logging

logger = logging.getLogger("yield_from_logger")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


class CustomException(Exception):
    pass


def sequence(name, start, end):
    value = start
    logger.info(f"{name} 제너레이터 {value}에서 시작")
    while value < end:
        try:
            received = yield value
            logger.info(f"{name} 제너레이터 '{received}' 값 수신")
            value += 1
        except CustomException as e:
            logger.info(f"{name} 제너레이터 {e} 에러 처리")
            received = yield "OK"
    return end


def collect_result():
    step1 = yield from sequence("first", 0, 5)
    step2 = yield from sequence("second", step1, 10)
    return step1 + step2


if __name__ == "__main__":
    generator = collect_result()

    try:
        print(next(generator))
        print(next(generator))  # received = None, 값은 1 리턴
        # 값 send를 서브 제너레이터인 sequence에 보내지 않고 collect_result 제너레이터에 보냈으나 yield from을 통해 sequence까지 데이터가 전달됨
        print(generator.send("첫번째 제너레이터를 위한 인자 값"))
        print(generator.throw(CustomException("처리 가능한 예외 던지기")))
        print(next(generator))
        print(next(generator))
        print(next(generator))
        print(next(generator))
        print(generator.throw(CustomException("두 번째 제너레이터를 향한 예외 던지기")))
    except StopIteration as e:
        print(f"returned value: {e.value}")     # returned value: 15
