# 모듈 : 함수, 변수, 클래스를 모아놓은 파일

# 파이썬에서 제공하는 모듈 사용
# 1 - 포함된 모든 함수 가져오기) import 모듈명
# 2 - 사용할 함수만 가져오기) from 모듈명 import 사용할 함수, 클래스...
# 3 - 별칭으로 가져오기) import 모듈명 as 별칭


# from math import sin, cos, floor, ceil

# # from 절을 사용하면 모듈명을 쓰지 않아도 함수를 사용할 수 있음
# print(ceil(3.14))
# print(sin(1))
# print(cos(1))
# print(floor(2.5))
# print(ceil(2.5))


import math as m

# as 별칭 사용 시 별칭.함수명으로도 모듈을 사용할 수 있음
print(m.ceil(3.14))
