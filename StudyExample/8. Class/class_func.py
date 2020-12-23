class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("===힉생 목록===")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

Student("윤인성", 97, 45, 66, 63)
Student("연하진", 56, 46, 77, 83)
Student("구지연", 97, 45, 66, 64)
Student("나선주", 97, 45, 66, 53)
Student("윤아린", 97, 45, 66, 73)
Student("윤명월", 97, 45, 66, 83)

Student.print()