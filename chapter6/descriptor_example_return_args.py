"""
MethodType
MethodType(callable, instance) 형태로 쓰임
- 첫번째 파라미터는 호출 가능한 객체여야 함 (이 예제에서 Method 객체는 __call__을 구현하였으므로 호출 가능한 객체임)
- 두번쨰 파라미터는 함수에 바인딩 할 객체
"""
from types import MethodType


class Method:
    def __init__(self, name):
        self.name = name

    def __call__(self, instance, arg1, arg2):
        print(f"{self.name}: {instance} 호출, arg1 = {arg1}, arg2 = {arg2}")

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return MethodType(self, instance)   # MethodType을 이용해 함수 -> 메서드 변환


class SampleClass:
    method = Method("객체 내부에서 초기화")


if __name__ == "__main__":
    instance = SampleClass()
    Method("객체 외부에서 초기화")(instance, '인자 1', '인자 2')
    instance.method('인자 1', '인자 2')     # Method 객체에 __get__을 구현하지 않으면 오류남.
