from functools import wraps


USER_LIST = ['A', 'B', 'C']


class NoAccessRightException(Exception):
    pass


def check_rule(function):
    @wraps(function)
    def wrapped(user_id):
        if user_id in USER_LIST:
            return function(user_id)
        else:
            raise NoAccessRightException(f"{user_id} does not have right to access credential contents")
    return wrapped


@check_rule
def access_credential(user_id):
    print(f"{user_id} can read credential contents")


# 메서드에는 데코레이터 적용 안됨
class Credential:
    @check_rule
    def access_credential(self, user_id):
        print(f"{user_id} can read credential contents")


if __name__ == "__main__":
    try:
        access_credential('A')
        access_credential('D')
    except NoAccessRightException as e:
        print(e)

    # 메서드에는 데코레이터 적용 안됨
    credential = Credential()
    credential.access_credential('B')
