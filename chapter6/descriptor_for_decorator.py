from functools import partial
from typing import Callable
from datetime import datetime


class BaseFieldTransformation:
    def __init__(self, transformation: Callable[[], str]) -> None:
        self._name = None
        self.transformation = transformation

    def __get__(self, instance, owner):
        if instance is None:
            return self
        raw_value = instance.__dict__[self._name]
        return self.transformation(raw_value)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value


# partial을 사용하면 partial(func, /, *args, **keywords) 형태로 사용되고, func에 대해 *args와 **keywords 들이 인자로 추가됨
# 아래의 경우 ShowOriginal을 초기화하면 BaseFieldTransformation(transformation=lambda x: x) 형태가 되는 것
ShowOriginal = partial(BaseFieldTransformation, transformation=lambda x: x)
HideField = partial(BaseFieldTransformation, transformation=lambda x: "**민감한 정보 삭제**")
FormatTime = partial(BaseFieldTransformation, transformation=lambda ft: ft.strftime("%Y-%m-%d %H:%M"))


class LoginEvent:
    # 각 필드들이 디스크립터로 구현되어있어서 __get__의 경우 transformation 함수가 적용된 값이 리턴됨
    username = ShowOriginal()
    password = HideField()
    ip = ShowOriginal()
    timestamp = FormatTime()

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def serialize(self):
        return {
            "username": self.username,
            "password": self.password,
            "ip": self.ip,
            "timestamp": self.timestamp
        }


if __name__ == "__main__":
    le = LoginEvent("john", "secret password", "1.1.1.1", datetime.utcnow())
    print(vars(le))
    print(le.serialize())
    le.password
