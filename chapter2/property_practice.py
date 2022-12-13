class Human(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 200 or age < 0:
            raise NotValidAgeException
        self._age = age


class NotValidAgeException(Exception):
    pass


if __name__ == "__main__":
    human = Human("Mary", 20)

    print(f"{human.name} is {human.age} years old")
    print("### 1 year later ###")

    human.age = human.age + 1
    print(f"{human.name} is {human.age} years old")
    print("### 200 year later ###")

    human.age = human.age + 200
