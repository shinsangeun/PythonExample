# 클래스 변수를 외부에서 사용할 수 있음

class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print("{}번째 학생이 생성 되었습니다.".format(Student.count))

students = [
    Student("윤인성", 97, 45, 66, 63),
    Student("연하진", 56, 46, 77, 83),
    Student("구지연", 97, 45, 66, 63),
    Student("나선주", 97, 45, 66, 63),
    Student("윤아린", 97, 45, 66, 63),
    Student("윤명월", 97, 45, 66, 63),
]

print()
print("현재 생성된 총 학생수는 {}명 입니다".format(Student.count))