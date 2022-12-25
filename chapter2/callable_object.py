class IncrementMachine:
    def __init__(self):
        self.counter = 0

    def __call__(self):
        self.counter += 1
        return self.counter


if __name__ == "__main__":
    increment_machine = IncrementMachine()
    print(increment_machine())
    print(increment_machine())
    print(increment_machine())
