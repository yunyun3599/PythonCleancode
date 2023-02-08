import time
import logging
from functools import wraps


# 로거 설정
log = logging.getLogger("decorator")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def wrong_time_calc(function):
    log.info(f"{function.__qualname__} starts at {time.strftime('%c', time.localtime())}")
    start_time = time.time()

    @wraps(function)
    def wrapped(*args, **kwargs):
        result = function(*args, **kwargs)
        log.info(f"총 수행 시간: {time.time() - start_time}")
        return result
    return wrapped


def right_time_calc(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        log.info(f"{function.__qualname__} starts at {time.strftime('%c', time.localtime())}")
        start_time = time.time()
        result = function(*args, **kwargs)
        log.info(f"총 수행 시간: {time.time() - start_time}")
        return result
    return wrapped


@wrong_time_calc
def wrong_sample_func(n: int):
    for _ in range(n):
        time.sleep(1)


@right_time_calc
def right_sample_func(n: int):
    for _ in range(n):
        time.sleep(1)


if __name__ == "__main__":
    time.sleep(2)
    wrong_sample_func(2)
    wrong_sample_func(1)

    right_sample_func(2)
    right_sample_func(1)
