# 클레스 예제
import sys

class Calculator:
    def __init__(self) -> None: # self는 안쓴다 클레스를 선언하기 위해서 쓰는 것이다 self가 들어가는 순간 얘는 class구나 알아야한다.
        self.result = 0

    def add(self, num): # 무조건 앞에 self를 무조건 앞에 적어햐한다.
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    def mul(self, num):
        pass
    
mycalc = Calculator() #java와 달리 new 없음
print(mycalc.add(40))
print(mycalc.add(50))
print(mycalc.add(15))

