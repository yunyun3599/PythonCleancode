from functools import wraps
import time
import logging

# 로거 설정
log = logging.getLogger("decorator")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


class TimeConsumed:
    def __init__(self, job_name: str, time_limit: int):
        self.job_name = job_name
        self.time_limit = time_limit

    def __call__(self, operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            start_time = time.time()
            operation(*args, **kwargs)
            elapsed_time = time.time() - start_time
            if (elapsed_time > self.time_limit):
                log.warning(f"{self.job_name} takes too long time: {elapsed_time} (time limit = {self.time_limit})")
        return wrapped


@TimeConsumed(job_name="sleep_n_seconds", time_limit=3)
def sleep_n_secs(n):
    for _ in range(n):
        time.sleep(1)


if __name__ == "__main__":
    sleep_n_secs(2)
    sleep_n_secs(3)

