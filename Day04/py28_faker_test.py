from faker import Faker
import pandas as pd

dummy = Faker('ko-KR')
print(dummy.name())
print(dummy.address())
print(dummy.company())

dummy_date = [(dummy.name(), dummy.postcode(), dummy.address(),
               dummy.phone_number(), dummy.email()) for i in range(100)]

df = pd.DataFrame(data=dummy_date, columns=['이름', '우편번호', '주소', '전화번호', '이메일'])
# print(dummy_data)
df.to_csv('./Day04/dummy_members.csv', index=True, encoding='utf-8')
print('CSV 생성완료!')