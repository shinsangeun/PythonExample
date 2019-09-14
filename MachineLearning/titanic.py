import pandas as pd

# csv 파일 읽기
titanic_df=pd.read_csv('train.csv')
titanic_df.head(3)

titanic_df = pd.read_csv('train.csv')
print('titanic 변수 type:', type(titanic_df))
titanic_df

titanic_df.head(3)

print('DataFrame 크기:',titanic_df.shape)

# 평균,최대,최소값 데이터 분포도 조회 함수
titanic_df.info()
titanic_df.describe()

# Pclass의 데이터 분포도 확인
value_counts=titanic_df['Pclass'].value_counts()
print(value_counts)

titanic_pclass=titanic_df['Pclass']
print(type(titanic_pclass))

titanic_pclass.head()

# 새로운 데이터 컬럼(Age_0) 생성
titanic_df['Age_0']=0
titanic_df.head(3)

# 기존 칼럼 Series의 데이터를 이용해 새로운 칼럼 생성(Age_by_10,Family_No)
titanic_df['Age_by_10']=titanic_df['Age']*10
titanic_df['Family_No']=titanic_df['SibSp']+titanic_df['Parch']
titanic_df.head(3)

# 새로운 칼럼 데이터 업데이트
titanic_df['Age_by_10']=titanic_df['Age_by_10']+100
titanic_df.head(3)

# 특정 칼럼 방향 축 삭제(Age_0 행 삭제)
titanic_drop_df=titanic_df.drop('Age_0', axis=1)
titanic_drop_df.head(3)

titanic_df.head(3)

# 데이터 로우 3개의 열 삭제
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth',15)
print('#### before axis 0 drop ####')
print(titanic_df.head(3))

titanic_df.drop([0,1,2], axis=0, inplace=True)

print('#### after axis 0 drop ####')
print(titanic_df.head(3))