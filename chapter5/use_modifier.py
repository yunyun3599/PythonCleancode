import time
import logging

# 로거 설정
log = logging.getLogger("decorator")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def origin():
    log.info(f"origin function start")
    for _ in range(5):
        time.sleep(1)
    log.info(f"origin function end")


def modifier(operation):
    log.info(f"modified origin func is assigned to origin at {time.strftime('%c', time.localtime())}")
    return operation


if __name__ == "__main__":
    origin()

    origin = modifier(origin)
    origin()
