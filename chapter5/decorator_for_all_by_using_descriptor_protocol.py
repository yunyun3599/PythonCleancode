from functools import wraps
from types import MethodType


USER_LIST = ['A', 'B', 'C']


class NoAccessRightException(Exception):
    pass


class check_rule:
    def __init__(self, function):
        self.function = function
        wraps(self.function)(self)

    def __call__(self, user_id):
        if user_id in USER_LIST:
            return self.function(user_id)
        else:
            raise NoAccessRightException(f"{user_id} does not have right to access credential contents")

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.__class__(MethodType(self.function, instance))  # MethodType(함수, 인스턴스)는 인스턴스에 메서드를 동적으로 추가할 수 있게 해줌


@check_rule
def access_credential(user_id):
    print(f"{user_id} can read credential contents")


class Credential:
    @check_rule
    def access_credential(self, user_id):
        print(f"{user_id} can read credential contents")


if __name__ == "__main__":
    credential = Credential()
    help(access_credential)
    try:
        access_credential('A')
        credential.access_credential('B')
        credential.access_credential('E')
    except NoAccessRightException as e:
        print(e)
