class Student:
    def __init__(self):
        self.id = None
        self.name = None
        self.age = None
        self.grade = None
        self.teacher = None


class StudentBuilder:
    def __init__(self):
        self.student = Student()

    def set_id(self, id):
        self.student.id = id
        return self

    def set_name(self, name):
        self.student.name = name
        return self

    def set_age(self, age):
        self.student.age = age
        return self

    def set_grade(self, grade):
        self.student.grade = grade
        return self

    def set_teacher(self, teacher):
        self.student.teacher = teacher
        return self

    def build(self):
        return self.student


if __name__ == "__main__":
    John = StudentBuilder()\
        .set_id("30321")\
        .set_name("John")\
        .set_age(16)\
        .set_grade(3)\
        .set_teacher("Colin")\
        .build()
    print(John.__dict__)
