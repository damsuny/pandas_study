from pandas import DataFrame

data = {'open': [737,750], 'high':[755,780], 'low':[700,710], 'close':[750,770]}		# 데이터(딕셔너리) 생성
df = DataFrame(data, index=["2021-06-03","2021-06-04"])									# 데이터프레임 생성(데이터, 인덱스)
print(df)

# 결과
#             open  high  low  close
# 2021-06-03   737   755  700    750
# 2021-06-04   750   780  710    770