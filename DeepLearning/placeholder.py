import tensorflow as tf

#플레이스 홀더 정의
a = tf.placeholder(tf.int32, [None])   #정수 자료형 3개를 가진 배열

#배열을 모든 값을 2배하는 연산 정의
b= tf.constant(10);
x2_op = a * b;

#세션 시작하기
sess = tf.Session();

r1 = sess.run(x2_op, feed_dict={ a:[1,2,3,4,5] })
print(r1)
r2 = sess.run(x2_op, feed_dict={ a:[10, 200] })
print(r2)


##############결과 값##################
#[10 20 30 40 50]
#[ 100 2000]
