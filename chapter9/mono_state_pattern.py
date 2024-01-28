class SharedAttribute:
    _shared_attribute = None

    def __init__(self, attribute):
        self.shared_attribute = attribute

    @property
    def shared_attribute(self):
        if self._shared_attribute is None:
            raise AttributeError("attribute가 초기화되지 않음")
        return self._shared_attribute

    @shared_attribute.setter
    def shared_attribute(self, new_attribute):
        self.__class__._shared_attribute = new_attribute

    def get_attribute(self):
        return self.shared_attribute


if __name__ == "__main__":
    print("### c1 인스턴스 공유속성 'one'으로 초기화 ###")
    c1 = SharedAttribute(attribute="one")
    print(f"c1의 공유 속성 값: {c1.get_attribute()}")

    print("\n### c2 인스턴스 공유속성 'two'로 초기화 ###")
    c2 = SharedAttribute(attribute="two")
    print(f"c1의 공유 속성 값: {c1.get_attribute()}")
    print(f"c2의 공유 속성 값: {c2.get_attribute()}")

    print("\n### c2 인스턴스 공유속성 'three'로 변경 ###")
    c2.shared_attribute = "three"
    print(f"c1의 공유 속성 값: {c1.get_attribute()}")
    print(f"c2의 공유 속성 값: {c2.get_attribute()}")
