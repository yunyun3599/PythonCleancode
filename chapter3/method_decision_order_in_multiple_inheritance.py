class BaseModule:
    module_name = "base"

    def __init__(self, module_name):
        self.name = module_name

    def __str__(self):
        return f"{self.module_name}: {self.name}"


class BaseModule1(BaseModule):
    module_name = "module-1"


class BaseModule2(BaseModule):
    module_name = "module-2"


class BaseModule3(BaseModule):
    module_name = "module-3"


class ConcreteModuleA12(BaseModule1, BaseModule2):
    """BaseModule1 + BaseModue2"""


class ConcreteModuleB23(BaseModule2, BaseModule3):
    """BaseModule2 + BaseModue3"""


class ConcreteModuleC32(BaseModule3, BaseModule2):
    """BaseModule3 + BaseModue2"""


class ConcreteModuleD321(BaseModule3, BaseModule2, BaseModule1):
    """BaseModule3 + BaseModue2"""


if __name__ == "__main__":
    print(str(ConcreteModuleA12("when BaseModule 1 is extended first")))
    print(str(ConcreteModuleB23("when BaseModule 2 is extended first")))
    print(str(ConcreteModuleC32("when BaseModule 3 is extended first")))
    print("ConcreteModuleA12:", [cls.__name__ for cls in ConcreteModuleA12.mro()])
    print("ConcreteModuleB23:", [cls.__name__ for cls in ConcreteModuleB23.mro()])
    print("ConcreteModuleC32:", [cls.__name__ for cls in ConcreteModuleC32.mro()])
    print("ConcreteModuleD321:", [cls.__name__ for cls in ConcreteModuleD321.mro()])
