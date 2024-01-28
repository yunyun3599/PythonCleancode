class DescriptorAttribute:
    def __init__(self, initial_value=None):
        self.value = initial_value
        self._name = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.value is None:
            raise AttributeError(f"{self._name} was never set")
        return self.value

    def __set__(self, instance, new_value):
        self.value = new_value

    def __set_name__(self, owner, name):
        self._name = name


class SharedAttribute:
    shared_attribute1 = DescriptorAttribute()
    shared_attribute2 = DescriptorAttribute()

    def __init__(self, attr1, attr2):
        self.shared_attribute1 = attr1
        self.shared_attribute2 = attr2

    def get_attribute1(self):
        return self.shared_attribute1

    def get_attribute2(self):
        return self.shared_attribute2


if __name__ == "__main__":
    print("### c1 인스턴스 공유속성 각각 'a', 'b'로 초기화 ###")
    c1 = SharedAttribute(attr1="a", attr2="b")
    print(f"c1의 공유 속성 1 값: {c1.get_attribute1()}")
    print(f"c1의 공유 속성 2 값: {c1.get_attribute2()}")

    print("\n### c2 인스턴스 공유속성 각각 'A', 'B'로 초기화 ###")
    c2 = SharedAttribute(attr1="A", attr2="B")
    print(f"c1의 공유 속성 1, 2 값: ({c1.get_attribute1()}, {c1.get_attribute2()})")
    print(f"c2의 공유 속성 1, 2 값: ({c2.get_attribute1()}, {c2.get_attribute2()})")

    print("\n### c2 인스턴스 공유속성 각각 'C', 'D'로 변경 ###")
    c2.shared_attribute1 = "C"
    c2.shared_attribute2 = "D"
    print(f"c1의 공유 속성 1, 2 값: ({c1.get_attribute1()}, {c1.get_attribute2()})")
    print(f"c2의 공유 속성 1, 2 값: ({c2.get_attribute1()}, {c2.get_attribute2()})")
