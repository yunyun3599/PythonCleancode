class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __walk(self):
        print(f"{self.name} is walking")

    def talk(self):
        print(f"{self.name} is talking")


class Student(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __walk(self):
        print(f"Student {self.name} is walking")

    def talk(self):
        print(f"Student{self.name} is talking")


class UniversityStudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __walk(self):
        print(f"University Student {self.name} is walking")

    def talk(self):
        print(f"University Student {self.name} is talking")


class ComputerScienceStudent(UniversityStudent):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __walk(self):
        super()._Human__walk()
        super()._Student__walk()
        super()._UniversityStudent__walk()
        print(f"Student {self.name} who is majoring in Computer Science is walking")

    def talk(self):
        super().talk()
        print(f"Student {self.name} who is majoring in Computer Science is talking")


if __name__ == "__main__":
    cs_student = ComputerScienceStudent("CS", 20)
    cs_student._ComputerScienceStudent__walk()
    print("\n######end walking#######\n")
    cs_student.talk()
