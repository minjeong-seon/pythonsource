# 변수 : 타입 없음 ==> 값 삽입 시 타입 결정됨
# 타입 : (숫자형) int, float
#       (문자형) str,
#       (논리형) bool,
#       (다양한 데이터 한번에 처리) list, set, dict, tuple                

# 문자열 - "", '', """한글""", '''한글'''

str1 = "Life is too short, You need Python"
str2 = 'Life is too short, You need Python'
str3 = """Life is too short, You need Python"""
str4 = '''Life is too short, You need Python'''

print(str1)
print(str2)
print(str3)
print(str4)

print()
num1 = num2 = 10    # 2개의 변수에 같은 값 대입
print(num1, num2)

num1, num2 = 10, 15    # 2개의 변수에 한번에 값 대입
print(num1, num2)
num1, num2 = num2, num1     # 2개의 변수에 들어있는 값 서로 바꾸기
print(num1, num2)

num1 = "한글"
print(num1)

#print(num1 + num2)  #  can only concatenate str (not "int") to str : int > str로 연결할 수 없음 에러
# 위의 오류 해결 : 숫자 => 문자열로 타입변환 == str() 사용
print(num1+str(num2))

# 연산자
a, b = 5,4
print("a + b = %d" % (a+b))
print("a - b = %d" % (a-b))
print("a * b = %d" % (a*b))
print("a / b = %f" % (a/b))     # 스크립트와 같은 개념, / 소숫점까지 나옴
print("a // b = %f" % (a//b))   # 자바와 같은 개념(몫), // 몫만 나옴
print("a % b = ", (a%b))
print("a ** b = ", (a**b))  # a ** b =  625 : a의 b제곱

# type() : 변수 타입 확인
# str() :  문자열 변환, int() : 숫자 변환, float() : 실수, bool() : 논리 변환
print(str(3.2), type(str(3.5)))         # 3.2 <class 'str'>
print(int(True), type(int(True)))       # 1 <class 'int'>
print(int(False), type(int(False)))     # 0 <class 'int'>
print(bool(0.1), type(bool(0.1)))       # True <class 'bool'>
print(float("98.99"), type(float("98.99")))     # 98.99 <class 'float'>

# 동전 교환
money, c500, c100, c50, c10 = 0,0,0,0,0

money = 7777

# 500원: 15개, 100원 2개, 50원 1개, 10원 2개, 나머지돈: 7원
c500 = money//500
money %= 500    # money는 500원으로 나눈 나머지

c100 = money//100
money %= 100

c50 = money//50
money %= 50

c10 = money//10
money %= 10

print("500원 : {} 개".format(c500))
print("100원 : {} 개".format(c100))
print("50원 : {} 개".format(c50))
print("10원 : {} 개".format(c10))
print("나머지 : {} 원".format(money))

# ||, && 사용 불가 --> or, and, not 써야 함
a, b, c = 100, 60, 15
print("and : ", a>b and a>c)
print("or : ", a>b or a>c)
print("not :", not(a>b))