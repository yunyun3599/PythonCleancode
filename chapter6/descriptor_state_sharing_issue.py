class Descriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        self.value = value


class ClientClass:
    descriptor = Descriptor("value 1")


if __name__ == "__main__":
    client1 = ClientClass()
    client2 = ClientClass()

    print("client1.descriptor:", client1.descriptor)
    print("client2.descriptor:", client2.descriptor)

    client2.descriptor = "client 2 value"

    print("\n####After changing value of client2.descriptor####")
    print("client1.descriptor:", client1.descriptor)
    print("client2.descriptor:", client2.descriptor)
