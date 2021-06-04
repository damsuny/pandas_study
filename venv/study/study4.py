from pandas import Series

s = Series([100,200,300,400])
print(s/10)							# 시리즈는 리스트, 딕셔너리, 튜플과 다르게 연산이 가능
# l = [100,200,300,400]
# print(l/10)      >>>>>>>>>> error

# 결과
# 0    10.0
# 1    20.0
# 2    30.0
# 3    40.0
# dtype: float64