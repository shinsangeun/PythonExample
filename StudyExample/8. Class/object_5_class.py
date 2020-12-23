# isinstance(): 어떤 클래스의 인스턴스 인지 확인하기
# 인스턴스가 해당 클래스를 기반으로 만들어졌다면 True, 상관 없는 인스턴스와 클래스라면 False를 리턴

class Student:
    def __init__(self):
        pass

class test:
    def __init__(self):
        pass

student = Student()

print("isinstance(student, Student):", isinstance(student, Student))