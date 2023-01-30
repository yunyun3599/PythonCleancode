import time
import logging
from functools import wraps


# 로거 설정
log = logging.getLogger("decorator")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def calc_time_consumed(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        log.info(f"function starts at {time.strftime('%c', time.localtime())}")
        return operation(*args, **kwargs)
    return wrapped


@calc_time_consumed
def origin(n: int):
    for _ in range(n):
        time.sleep(1)


if __name__ == "__main__":
    origin(3)
