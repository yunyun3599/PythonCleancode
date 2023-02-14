class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return f"Instance is None: {self.__class__.__name__}, {owner.__name__}"
        return f"Call descriptor from {instance}"


class ClientClass:
    descriptor = DescriptorClass()


if __name__ == "__main__":
    print(ClientClass.descriptor)
    print(ClientClass().descriptor)
