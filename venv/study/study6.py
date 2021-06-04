import pandas as pd

df = pd.read_excel('ohlc.xlsx')					# 엑셀 파일을 불러와서 데이터 프레임 생성
# 엑셀을 읽어올 때는 read_excel, 엑셀을 저장할 때는 to_excel 함수를 사용한다.
print(df)										# 데이터 프레임 출력

print('*'*80)

df = df.set_index('date')						# auto_increment 넘버를 제외하고 인덱스를 date로 설정
print(df)										# 위의 df 와 비교

# 결과
#         date  open  high  low  close
# 0 2021-06-02   100   110   70    100
# 1 2021-06-03   200   210  180    190
# 2 2021-06-04   300   310  300    310
# ********************************************************************************
#             open  high  low  close
# date
# 2021-06-02   100   110   70    100
# 2021-06-03   200   210  180    190
# 2021-06-04   300   310  300    310
