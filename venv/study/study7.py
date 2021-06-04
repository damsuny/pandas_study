import pandas as pd

url = "https://finance.naver.com/item/main.nhn?code=000660"
df = pd.read_html(url)			# read_html() 함수는 웹페이지를 데이터 프레임으로 변환 해줍니다.
print(df[0].dropna(axis=0))							# na를 걸러내기 위해 dropna를 사용합니다.

# 결과
#                         0  ...                                 2
# 0  ÀüÀÏ  129,000  129,000  ...      °Å·¡·®  2,551,057  2,551,057
# 1    ½Ã°¡  127,500127,500  ...  °Å·¡´ë±Ý  325,602  325,602  ¹é¸¸
#
# [2 rows x 3 columns]

# 결과를 보면 알 수 없는 문자로 출력 되어 있는 것을 볼 수 있다. encoding 방식이 달라서 그런거 같다. 그런데 어떻게 변환하는지 잘 모르겠다.

# read_html에 대해서 문서를 읽어본 결과 encoding 방식을 변경할 수 있었다.

df = pd.read_html(url,encoding='EUC-KR')			# 해당 url에서 encoding 방식 그대로 가져오면 한글이 깨지지 않고 잘 나온다.
print(df[0].dropna(axis=0))

# 결과
#                       0  ...                           2
# 0  전일  129,000  129,000  ...   거래량  2,551,057  2,551,057
# 1    시가  127,500127,500  ...  거래대금  325,602  325,602  백만
#
# [2 rows x 3 columns]

# 한글이 잘 나온다. 해당 url의 encoding 방식과 같은 방식으로 바꿔주면 잘 나온다. 편안하다.