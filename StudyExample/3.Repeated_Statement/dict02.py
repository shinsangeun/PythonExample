dictionary={}

print("요소 추가 이전:",dictionary)

dictionary["name"]="새로운 이름"
dictionary["type"]="새로운 타입"
dictionary["content"]="새로운 내용"

print("요소 추가 이후:",dictionary)

del dictionary["name"]

print("요소 삭제 이후:",dictionary)