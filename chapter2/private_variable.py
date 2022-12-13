class Something:
    def __init__(self, public_value, private_value):
        self.public = public_value
        self._private = private_value


if __name__ == "__main__":
    sth = Something(10, 20)
    print("_private:", sth._private)
    print(sth.__dict__)
