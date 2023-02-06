from functools import wraps
import time
import logging

# 로거 설정
log = logging.getLogger("decorator")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def consumed_time(job_name: str, time_limit: int):
    def calc(operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            start_time = time.time()
            operation(*args, **kwargs)
            elapsed_time = time.time() - start_time
            if (elapsed_time > time_limit):
                log.warning(f"{job_name} takes too long time: {elapsed_time} (time limit = {time_limit})")
        return wrapped
    return calc


@consumed_time(job_name="sleep_n_seconds", time_limit=3)
def sleep_n_secs(n):
    for _ in range(n):
        time.sleep(1)


if __name__ == "__main__":
    sleep_n_secs(2)
    sleep_n_secs(3)
