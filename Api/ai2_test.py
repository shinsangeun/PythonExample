import pandas as pd
import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

df = pd.read_csv('ai3.csv')
print(df.head(3))

dataFrame={
    "x":df["x"],
    "y":df["y"],
    "z":df["z"],
    "result":df["result"]
}

data=df[["x","y","z"]].values.tolist()
print(df)

label=df["result"].values.tolist()
print(label)

x=data
y=label
print(x)
print(y)

data_train, data_test, label_train, label_test = train_test_split(data, label)

# 학습 진행
forest = RandomForestClassifier(n_estimators=100)
forest.fit(data_train, label_train)

# 데이터 예측
y_pred = forest.predict(data_test)
print(data_test)
print("예측: ",y_pred)

# 모델 저장
from sklearn.externals import joblib
joblib.dump(forest, 'model.pkl')

# 정확도
ac_score = metrics.accuracy_score(label_test, y_pred)
print("정확도: ", ac_score)
