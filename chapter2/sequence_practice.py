class Classroom:
    def __init__(self, student_list: list):
        self._student_names = student_list

    def __len__(self):
        return len(self._student_names)

    def __getitem__(self, student_number):
        return self._student_names.__getitem__(student_number)


if __name__ == "__main__":
    classroom = Classroom(["Kang", "Kim", "Park", "Song", "Lee", "Jeon", "Choi", "Hwang"])
    print(len(classroom))
    print(classroom[0])
    print(classroom[6:])
