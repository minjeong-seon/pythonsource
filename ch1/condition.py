# 조건문
# if, if~else, if~elif~else
if True:
    print("True")

a = 200
if a < 100:
    print("a는 100보다 작다.")
print("조건문에서 하나의 블럭 개념은 들여쓰기로 구분")


# a는 100보다 크고 200보다 작거나 같다
if 100 < a <= 200:  # a > 100 and 2 <= 200
    print("a는 100보다 크고 200보다 작거나 같다.")


# 세 개의 변수 선언 : 12, 6, 18 값 담아서 가장 큰 수 찾기
x, y, z = 12, 6, 18
max = x
if max < y:
    max = y
if max < z:
    max = z
print("가장 큰 수 : {}".format(max))

a = 55
if a < 100:
    print("a는 100보다 작다")
else:
    print("a는 100보다 크다")


# 숫자 입력받은 후 짝, 홀 구분하여 출력
# num1 = int(input("숫자 입력: "))
# if num1%2==0:
#     print("num1 : 짝수")
# else:
#     print("num1 : 홀수")


import datetime

now = datetime.datetime.now()
print(now)  # 2023-06-14 11:55:34.544536

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
# 2023년 6월 14일 11시 55분 34초


# 현재 시간이 오전인지 오후인지 출력
if now.hour < 12:
    print("오전")
else:
    print("오후") 


# 삼항연산자
# 참일 때 실행 구문 if 조건 else 거짓일 때 실행구문
str = "안녕하세요" if True else "반갑습니다"
print(str)
print("오전" if now.hour < 12 else "오후")


# 다중 조건 : if ~ elif ~ else
num = 90

if num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("F")


# age, height 변수 선언 = 27, 180 값 담기
# 나이가 20세 이상이면 지원 가능 + 키가 170 이상이면 A지망 지원 가능
# 나이가 20세 이상이면 지원 가능 + 키가 160 이상이면 B지망 지원 가능
# 나머지 키는 지원 불가
# 나이가 20세 미만이면 20세 이상 지원 가능 출력

age, height = 27, 180

if age>=20:
    if height >= 170: print("A지망 지원 가능")
    elif height >= 160: print("B지망 지원 가능")
    elif height <160: print("지원 불가")
else:
    print("20세 이상만 지원 가능")

print()



# 사칙연산 계산기 : 2개의 수와 연산자(+, -, *, /, //, %) 입력받기

a = int(input("a: "))
op = input("연산자 입력: ")
b = int(input("b: "))


if op == '+':
    result = a+b
elif op == '-':
    result = a-b
elif op == '*':
    result = a*b
elif op == '/':
    result = a/b
elif op == '%':
    result = a%b
elif op == '//':
    result = a//b
elif op == '**':
    result = a**b

print("{} {} {} = {}".format(a,op,b,result))

