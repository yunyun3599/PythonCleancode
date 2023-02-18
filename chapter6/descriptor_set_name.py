class DescriptorWithoutSetName:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class DescriptorWithSetName:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class ClientClass:
    descriptor_without_set_name = DescriptorWithoutSetName('descriptor_without_set_name')
    descriptor_with_set_name = DescriptorWithSetName()


if __name__ == '__main__':
    client = ClientClass()

    client.descriptor_without_set_name = 'without value'
    client.descriptor_with_set_name = 'with value'
    print(client.descriptor_with_set_name)
    print(client.descriptor_without_set_name)
