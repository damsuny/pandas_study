from pandas import Series

data = [100,200,300,400]
s = Series(data)                # data를 판다스의 series로 묶어줍니다.
print(s)
print(type(s))

# 결과
# 0    100
# 1    200
# 2    300
# 3    400
# dtype: int64
# <class 'pandas.core.series.Series'>