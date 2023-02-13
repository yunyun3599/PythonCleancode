from functools import wraps


USER_LIST = ['A', 'B', 'C']


class NoAccessRightException(Exception):
    pass


def check_rule(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        user_id = kwargs['user_id']
        if user_id in USER_LIST:
            return function(*args, **kwargs)
        else:
            raise NoAccessRightException(f"{user_id} does not have right to access credential contents")
    return wrapped


@check_rule
def access_credential(user_id):
    print(f"{user_id} can read credential contents")


class Credential:
    @check_rule
    def access_credential(self, user_id):
        print(f"{user_id} can read credential contents")


if __name__ == "__main__":
    try:
        access_credential(user_id='A')
        access_credential(user_id='D')
    except NoAccessRightException as e:
        print(e)

    credential = Credential()
    credential.access_credential(user_id='B')
