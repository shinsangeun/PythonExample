class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

students = [
    Student("윤인성", 97, 45, 66, 63),
    Student("연하진", 56, 46, 77, 83),
    Student("구지연", 97, 45, 66, 63),
    Student("나선주", 97, 45, 66, 63),
    Student("윤아린", 97, 45, 66, 63),
    Student("윤명월", 97, 45, 66, 63),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())