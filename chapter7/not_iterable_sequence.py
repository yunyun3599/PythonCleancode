class NotIterableSequence:
    def __init__(self, start, step):
        self.current = start
        self.step = step

    def __next__(self):
        value = self.current
        self.current += self.step
        return value


if __name__ == "__main__":
    sequence = NotIterableSequence(0, 10)
    print(next(sequence))
    print(next(sequence))
    print(next(sequence))

    for value in NotIterableSequence(0, 10):
        print(value)
