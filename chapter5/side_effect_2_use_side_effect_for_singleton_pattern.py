BEAN_OBJECT = {}


def register_bean(cls):
    """하나의 인스턴스만 쓸 클래스 등록"""
    BEAN_OBJECT[cls.__name__] = cls()
    return BEAN_OBJECT[cls.__name__]


@register_bean
class Registry:
    """Bean 등록 Registry"""
    def __init__(self):
        self.name = 'repository'


@register_bean
class Controller:
    """Bean 등록 Controller"""


@register_bean
class Service:
    """Bean 등록 Service"""


if __name__ == "__main__":
    print(BEAN_OBJECT)
    print(BEAN_OBJECT['Registry'])
    print(BEAN_OBJECT['Registry'].name)
