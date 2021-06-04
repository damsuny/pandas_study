from pandas import Series

s1 = Series([100,200,300])			# series 생성
s2 = s1.shift(1)					# s1 데이터를 1행씩 뒤로 미룸(존재하는 행에만 데이터가 남는다.)
s3 = s1.shift(-1)					# s1 데이터를 1행씩 앞으로 당김(존재하는 행에만 데이터가 남는다.)
print(s1)
print(s2)
print(s3)

# 결과
# 0    100
# 1    200
# 2    300
# dtype: int64
# 0      NaN
# 1    100.0
# 2    200.0
# dtype: float64
# 0    200.0
# 1    300.0
# 2      NaN
# dtype: float64