class Example:
    def __init__(self, x):
        self.x = x

    def method(self):
        self.x = self.x + 1
        return self.x


def func(instance):
    instance.x = instance.x + 1
    return instance.x


if __name__ == "__main__":
    example = Example(1)
    print(example.method())
    print(Example.method(example))
    print(func(example))
