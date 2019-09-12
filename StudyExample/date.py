import datetime

now = datetime.datetime.now()

print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.minute,"분")
print(now.second,"초")

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

if now.hour < 12:
    print("현재 시각은 {}시 이므로 오전 ㅇㅂ니다".format(now.hour))

if now.hour >12:
    print("현재 시각은 {}시 이므로 오후 입니다".format(now.hour))

if 3 <= now.month <= 5:
    print("이번달은 {}월로 봄 입니다.".format(now.month))

if 6 <= now.month <=8:
    print("이번달은 {}월로 여름 입니다.".format(now.month))

if 9 <= now.month <=11:
    print("이번달은 {}월로 가을 입니다.".format(now.month))

if 12 <= now.month <=2:
    print("이번달은 {}월로 겨울 입니다.".format(now.month))