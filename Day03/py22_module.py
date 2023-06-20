# 모듈 사용
# import datetime as dt
from datetime import datetime # as dt
from os import getcwd


curr_date = datetime.now() #dt.datetime.now() -> dt.now() 이렇게 줄일 수 있다.
print(curr_date)
print(getcwd())