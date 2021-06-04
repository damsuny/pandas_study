from pandas import DataFrame, Series

data = {"open":[730,750],"high":[755,780],"low":[700,710],"close":[750,770]}	# 딕셔너리 생성
df = DataFrame(data, index=["2021-06-03","2021-06-04"])				# 데이터 프레임 생성
print(df)															# 데이터 프레임 출력
print('*'*80)
print(df["open"])													# 데이터 프레임에서 open 만 출력
print('*'*80)
print(df.loc["2021-06-04"])											# loc 는 특정 행을 불러온다.
print('*'*80)
print(df.iloc[1])													# iloc 는 auto_increments 값으로 특정 행을 불러온다.
print('*'*80)
target = ["2021-06-03","2021-06-04"]
print(df.loc[target])												# list 형태로 target을 줘도 행을 특정해서 불러온다.
print('*'*80)
target = [0,1]
print(df.iloc[target])												# list 형태로 target을 줘도 행을 특정해서 불러온다.
print('*'*80)

# 데이터 프래임에 새로운 column 추가 하기(series 를 만들어 추가한다.)
data = {"open":[730,750],"high":[755,780],"low":[700,710],"close":[750,770]}
df = DataFrame(data)
s = Series([300, 400])
df["volum"] = s														# volume 열을 추가
print(df)
print('*'*80)
df.loc[2] = (100,200,300,400,500)									# 2번째(0부터 시작) 행에 데이터 추가
print(df)
print('*'*80)

# 기존 데이터를 활용한 열 추가
upper = df["open"] * 1.3
df["upper"] = upper
print(df)