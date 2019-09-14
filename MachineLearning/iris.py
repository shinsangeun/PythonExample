from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
# DecisionTreeRegressor -> DecisionTreeClassfier 하면 에러나서 바꿈


import pandas as pd

iris=load_iris()

iris_data=iris.data

iris_label=iris.target
print('iris target 값:', iris_label)
print('iris target 명:', iris.target_names)

iris_df=pd.DataFrame(data=iris_data, columns=iris.feature_names)
iris_df['label']=iris.target
iris_df.head(3)

# 학습 데이터 분할
X_train, X_test, y_train, y_test=train_test_split(iris_data, iris_label,
                                                  test_size=0.2, random_state=11)

df_clf=DecisionTreeRegressor(random_state=11)

# 학습수행
df_clf.fit(X_train, y_train)

# 학습이 완료된 DecisionTreeRegressor 객체에서 테스트 데이터 세트로 예측 수행
pred=df_clf.predict(X_test)

# 예측 정확도 도출
from sklearn.metrics import accuracy_score
print('예측 정확도:{0:.4f}'.format(accuracy_score(y_test,pred)))