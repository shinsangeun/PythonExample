import pandas as pd
import numpy as np
import tensorflow as tf

csv = pd.read_csv("bmi.csv")
csv["height"] = csv["height"] / 200
csv["weight"] = csv["weight"] / 100

# - thin = (1,0,0) / normal = (0,1,0) / fat = (0,0,1)
bclass = {"thin": [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
csv["label_pat"] = csv["label"].apply(lambda x: np.array(bclass[x]))

test_csv = csv[15000:20000]
test_pat =test_csv[["weight", "height"]]
test_ans = list(test_csv["label_pat"])

x = tf.placeholder(tf.float32, [None, 2])
y_ = tf.placeholder(tf.float32, [None, 3])

W = tf.Variable(tf.zeros([2,3]));    #가중치
b = tf.Variable(tf.zeros([3]));        #바이어스

#소프트맥스 회귀 정의
y = tf.nn.softmax(ft.matmul(x,W)+b)

#모델 훈련
cross_entropy = -tf.reduce_sum(y_ *tf.log(y))
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(cross_entropy)

#정답률 구하기
predict = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

#세션 시작
sess = tf.Session()
sess.run(tf.tf.global_variables_initializer())     #변수 초기화
#학습 시키기
for step in range(3500):
    i = (step * 100) % 14000
    rows = csv[1 + i : 1 + i + 100]
    x_pat = rows[["weight", "height"]]
    y_ans = list(rows["label_pat"])
    fd = {x: x_pat, y: y_ans}
    sess.run(train, feed_dict = fd)
    if setp % 500 == 0:
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict = {x: x_pat, y: y_ans})
        print("step=", step, "cre= ", cre, "acc=",acc)
        
#최종 정답률
acc = sess.run(accuracy, feed_dict={x: x_pat, y: y_ans})
print("정답률= ", acc)
