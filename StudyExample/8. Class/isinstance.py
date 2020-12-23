class Student:
    def study(self):
        print("공부를 합니다")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다")

classRoom = [Student(), Student(), Student(), Teacher(), Student()]

for person in classRoom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()