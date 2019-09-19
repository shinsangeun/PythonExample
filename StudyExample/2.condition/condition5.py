import datetime

now=datetime.datetime.now()
month=now.month

if 3<=month<=5:
    print("현재는 봄 입니다.")
elif 6<=month<=8:
    print("현재는 여름 입니다.")
elif 9<=month<=11:
    print("현재는 가을 입니다.")
else:
    print("현재는 겨울 입니다.")