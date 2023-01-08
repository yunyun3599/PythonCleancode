class BaseModule:
    module_name = "base"

    def __init__(self, explanation):
        self.explanation = explanation

    def __str__(self):
        return f"{self.module_name}: {self.explanation}"


class BaseModule1(BaseModule):
    module_name = "module-1"


class BaseModule2(BaseModule):
    module_name = "module-2"


class BaseModule3(BaseModule):
    module_name = "module-3"


class ConcreteModule12(BaseModule1, BaseModule2):
    """BaseModule1 + BaseModue2"""


class ConcreteModule23(BaseModule2, BaseModule3):
    """BaseModule2 + BaseModue3"""


class ConcreteModule32(BaseModule3, BaseModule2):
    """BaseModule3 + BaseModue2"""


class ConcreteModule321(BaseModule3, BaseModule2, BaseModule1):
    """BaseModule3 + BaseModue2"""


if __name__ == "__main__":
    print(str(ConcreteModule12("when BaseModule 1 is extended first")))
    print(str(ConcreteModule23("when BaseModule 2 is extended first")))
    print(str(ConcreteModule32("when BaseModule 3 is extended first")))
    print("ConcreteModule12:", [cls.__name__ for cls in ConcreteModule12.mro()])
    print("ConcreteModule23:", [cls.__name__ for cls in ConcreteModule23.mro()])
    print("ConcreteModule32:", [cls.__name__ for cls in ConcreteModule32.mro()])
    print("ConcreteModule321:", [cls.__name__ for cls in ConcreteModule321.mro()])
