# 모듈 : 함수, 변수, 클래스를 모아놓은 파일

# 파이썬에서 제공하는 모듈 사용
import math  # 모듈 전체를 불러오기

# print(dir(math))  # math 모듈에 포함된 함수 목록 디렉토리로 펼쳐 보기

# # ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


# print(math.ceil(3.14))
# print(math.sin(1))
# print(math.cos(1))
# print(math.floor(2.5))
# print(math.ceil(2.5))


import random

# 0.0 <= x < 1 리턴
# print(random.random())
# # 10 ~ 20 사이 임의의 수 float 리턴
# print(random.uniform(10, 20))
# # 0 ~ 지정값 사이의 수 int 리턴
# print(random.randrange(10))
# # 리스트 안의 임의의 수 리턴
# print(random.choice([1,2,3,4,5,6]))


# list1 = list(range(10,20))
# print("생성된 리스트",list1)    # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# # 리스트 안의 요소 셔플하기
# random.shuffle(list1)
# print("셔플 리스트",list1)  # [11, 12, 19, 17, 14, 15, 16, 13, 10, 18]

# # 리스트에서 임의의 숫자 k 개만큼 추출
# print(random.sample(list1, k=2))    # [16, 19]


import time

print("지금부터 5초 정지합니다.")
time.sleep(5)
print("프로그램 종료")
