class Something:
    def __init__(self, value):
        self.__var = value


if __name__ == "__main__":
    sth = Something(30)
    print(sth.__dict__)
    print(sth.__var)
