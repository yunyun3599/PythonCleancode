class DataDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return "descriptor value"

    def __set__(self, instance, value):
        instance.__dict__['descriptor'] = value


class ClientClass:
    descriptor = DataDescriptor()


if __name__ == "__main__":
    client = ClientClass()
    print(client.descriptor)    # descriptor value

    client.descriptor = "new_value"
    print(client.descriptor)    # descriptor value
    print(vars(client))         # {'descriptor': 'new_value'}

    del client.descriptor       # Error
