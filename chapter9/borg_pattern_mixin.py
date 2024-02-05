class SharingMixin:
    def __init__(self, *args, **kwargs):
        try:
            self.__class__._attributes
        except AttributeError:
            self.__class__._attributes = {}
        self.__dict__ = self.__class__._attributes
        super().__init__(*args, **kwargs)


class ParentBorgClass:
    def __init__(self, common_attribute):
        self.common_attribute = common_attribute


class BorgClass1(SharingMixin, ParentBorgClass):
    def get_attributes(self):
        return f"common_attribute = {self.common_attribute}"


class BorgClass2(SharingMixin, ParentBorgClass):
    def get_attributes(self):
        return f"common_attribute = {self.common_attribute}"


if __name__ == "__main__":
    print("#### BorgClass1 Example ####")
    c11 = BorgClass1(common_attribute="c11_common_attribute")
    print(f"c11's {c11.get_attributes()}")          # c11's common_attribute = c11_common_attribute

    print("\ncreate c12 class")
    c12 = BorgClass1("c12_common_attribute")
    print(f"c11's {c11.get_attributes()}")          # c11's common_attribute = c12_common_attribute
    print(f"c12's {c12.get_attributes()}")          # c12's common_attribute = c12_common_attribute

    print("\nchange value of common attribute")
    c11.common_attribute = "c1 new common value"
    print(f"c11's {c11.get_attributes()}")          # c11's common_attribute = c1 new common value
    print(f"c12's {c12.get_attributes()}")          # c12's common_attribute = c1 new common value

    print("\n\n#### BorgClass2 Example ####")
    c21 = BorgClass2(common_attribute="c21_common_attribute")
    print(f"c21's {c21.get_attributes()}")          # c21's common_attribute = c21_common_attribute

    print("\ncreate c22 class")
    c22 = BorgClass2("c22_common_attribute")
    print(f"c21's {c21.get_attributes()}")          # c21's common_attribute = c22_common_attribute
    print(f"c22's {c22.get_attributes()}")          # c22's common_attribute = c22_common_attribute

    print("\nchange value of common attribute")
    c21.common_attribute = "c2 new common value"
    print(f"c21's {c21.get_attributes()}")          # c21's common_attribute = c2 new common value
    print(f"c22's {c22.get_attributes()}")          # c22's common_attribute = c2 new common value


