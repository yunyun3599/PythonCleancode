class BorgClass:
    _attributes = {}

    def __init__(self):
        self.__dict__ = self.__class__._attributes

    def get_attributes(self):
        return f"self._dict__ = {self.__dict__}"


if __name__ == "__main__":
    cl1 = BorgClass()
    cl1.common_attribute = "common1"
    print(cl1.get_attributes())     # self._dict__ = {'common_attribute': 'common1'}

    print("\ncreate c2 class")
    cl2 = BorgClass()
    print(cl1.get_attributes())     # self._dict__ = {'common_attribute': 'common1'}
    print(cl2.get_attributes())     # self._dict__ = {'common_attribute': 'common1'}

    print("\nchange value of common attribute")
    cl1.common_attribute = "new common value"
    print(cl1.get_attributes())     # self._dict__ = {'common_attribute': 'new common value'}
    print(cl2.get_attributes())     # self._dict__ = {'common_attribute': 'new common value'}


