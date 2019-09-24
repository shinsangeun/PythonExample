dictionary = {
    "name":"7D 건망고",
    "type":"당 절임",
    "ingredient":["망고","설탕","메타중아황상산나트륨","치자황색소"],
    "origin":"필리핀"
}

key=input("> 접근하고자 하는 키:")

if key in dictionary:
    print(dictionary[key])
else:
    print("접근할 키가 존재하지 않습니다.")