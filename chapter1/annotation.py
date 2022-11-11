from typing import List


class Semester:
    lecture_list: List
    minimum: int

    def __init__(self, lecture_list: List, minimum: int):
        self.lecture_list = lecture_list
        self.minimum = minimum

    def can_register(self, lecture: str, credit: int) -> bool:
        """강의 수강이 가능한 지 bool 리턴"""
        if lecture in self.lecture_list and credit >= self.minimum:
            return True
        return False


semester = Semester(['algorithm', 'network', 'database', 'software engineering', 'artificial intelligence'], 3)
print(Semester.__annotations__)
print(semester.can_register.__annotations__)
print(semester.can_register('algorithm', 3))
print(semester.can_register('network', 1))
print(semester.can_register('operating system', 5))
