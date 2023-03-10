class IterableSequence:
    def __init__(self, start, step):
        self.current = start
        self.step = step

    def __next__(self):
        value = self.current
        self.current += self.step
        return value

    def __iter__(self):
        return self


if __name__ == "__main__":
    sequence = IterableSequence(0, 10)
    print(next(sequence))
    print(next(sequence))
    print(next(sequence))

    for value in IterableSequence(0, 10):
        if value > 100:
            break
        print(value)
