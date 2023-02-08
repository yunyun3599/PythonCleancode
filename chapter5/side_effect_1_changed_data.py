import logging
from functools import wraps

# 로거 설정
log = logging.getLogger("decorator")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def wrong_logger(function):
    def wrapped(*args, **kwargs):
        log.info(f"{function.__qualname__} 실행")
        return function(*args, **kwargs)
    return wrapped


def right_logger(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        log.info(f"{function.__qualname__} 실행")
        return function(*args, **kwargs)
    return wrapped


@wrong_logger
def wrong_sample_func():
    """This is a sample function"""
    pass


@right_logger
def right_sample_func():
    """This is a sample function"""
    pass


if __name__ == "__main__":
    print("wrong_sample_func.__qualname__:", wrong_sample_func.__qualname__)
    wrong_sample_func()
    help(wrong_sample_func)
    print()
    print("right_sample_func.__qualname__:", right_sample_func.__qualname__)
    right_sample_func()
    help(right_sample_func)

