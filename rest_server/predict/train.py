import pandas as pd
import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.externals import joblib
from flask import jsonify, request
import traceback

df = pd.read_csv('20190926.csv')
print(df.head(3))

dataFrame={
    "x":df["ACCELER_X_AXIS"],
    "y":df["ACCELER_Y_AXIS"],
    "z":df["ACCELER_Z_AXIS"],
    "result":df["result"]
}
#print(dataFrame)

#df_list=df.values.tolist()
#print(df_list)

data=df[["ACCELER_X_AXIS","ACCELER_Y_AXIS","ACCELER_Z_AXIS"]].values.tolist()
# print(df)

label=df["result"].values.tolist()
#print(label)

x=data
y=label
#print(x)
#print(y)

data_train, data_test, label_train, label_test = train_test_split(data, label)

# 학습 진행
forest = RandomForestClassifier(n_estimators=100)
forest.fit(data_train, label_train)

# 예측
label_pred = forest.predict(data_test)
#print(data_test)
#print(label_pred)
#print(list(label_test))

# 모델 저장
joblib.dump(forest, '../model/model.pkl')

# 데이터 예측하기
predict = forest.predict(data_test)
#print(data_test)

# 결과 테스트하기
ac_score = metrics.accuracy_score(label_test, predict)
print("정확도 =", ac_score)
print("predict =\n", predict)
