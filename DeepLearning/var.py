import tensorflow as tf

#상수 정의
a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")

#변수 정의
v =tf.Variable(0,name="v")

#데이터 플로우 그래프 정의하기
clac_op = a + b + c
assign_op = tf.assign(v, clac_op)

#세션 실행
sess = tf.Session()
sess.run(assign_op)

#v의 내용 출력
print( sess.run(v))
