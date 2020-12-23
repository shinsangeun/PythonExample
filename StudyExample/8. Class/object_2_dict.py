def create_student(name, korean, math, english, science):
    return{
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

students = [
    create_student("윤인성", 97, 45, 66, 63),
    create_student("연하진", 56, 46, 77, 83),
    create_student("구지연", 97, 45, 66, 63),
    create_student("나선주", 97, 45, 66, 63),
    create_student("윤아린", 97, 45, 66, 63),
    create_student("윤명월", 97, 45, 66, 63),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")