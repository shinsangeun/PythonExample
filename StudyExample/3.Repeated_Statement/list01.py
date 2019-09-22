list_a=[1,2,3]
list_b=[4,5,6]

print("# 리스트")
print("list_a=", list_a)
print("lisb_b=", list_b)

# 리스트 연결
print(list_a + list_b)

# 리스트 반복
print(list_a * 3)

# 리스트 길이
print(len(list_a))

# 리스트 뒤에 요소 추가
list_a.append(4)
list_b.append(5)

print(list_a, list_b)
print()

# 리스트 중간에 요소 추가
list_a.insert(3,10)
print(list_a)