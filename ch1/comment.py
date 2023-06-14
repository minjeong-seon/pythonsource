# 주석
"""여러줄 주석 처리"""
'''여러줄 주석 처리'''

# print() : 화면 출력
# type() : 변수 타입 확인
print("Hello Python!!!")
print("123")
print(7)
print(type(130613))    # <class 'int'>
print(type("0613")) # <class 'str'>
print(type(06.13))  # <class 'float'>
print(type(True))   # <class 'bool'>

# sep= : 문자열 사이 구분자(기본값: spacebar)
print('t','e','s','t')  # t e s t (사이 띄기 해줌)
print('t','e','s','t', sep="")  # test (붙여서 출력)
print('t','e','s','t', sep="-") # t-e-s-t

# end= : 출력문 끝나는 값 지정(기본값: enter)
print('welcome to', end=' ')
print('the black prade')    # welcome to the black prade                                     

# format : %s(문자열, 정수, 실수 다 됨), %d(정수), %f(실수), %c(문자열 하나)
print("%d" %100)    # 100
print("%5d" %100)   #   100 (5자리 맞춰서 출력(우측정렬))
print("%05d" %100)  # 00100 (비어있는 자릿수는 0으로 채움)
print()
print("%s" %"hi")
print("%5s" %"hi")
print()
print("%-8.2f" % 123.21)    # -붙이면 왼쪽 정렬
print("%8.2f" % 123.21)     # 정수는 8자리, 소수는 2자리
print("%8.2f" % 123.213456) #   123.21

# 변수 선언(타입 선언 x) = 값에 따라 타입이 결정됨
number = 3
print("I ate %d apples" % number)   # I ate 3 apples
print("I ate", number, "apples")    # I ate 3 apples

# TypeError: not enough arguments for format string
# print("%d : %s" % 1, "홍길동")
print("%d : %s" % (1, "홍길동"))    # (포맷 여러개 사용할 때는 괄호로 묶어야 함)

# 98% 를 출력하고 싶을 때
#print("Error is%d%" % 98)   #ValueError: incomplete format
print("Error is %d%%" % 98) 

# format() 함수 : index 지정 가능
print("\nformat 함수: {}")
print("{} and {}".format("U","Me"))
print("I ate {} apples".format(3))
print("I ate {0} apples".format(3))
print("{0} and {1} and {0}".format("U","Me"))   # 인덱스 : {} - 정수로 지정 시 => 0부터 시작
print("{var1} and {var2}".format(var1="U",var2="Me"))   # 변수로 인덱스 지정 가능
print("{0} and {var2}".format("U",var2="Me"))   # 정수 인덱스, 변수 인덱스 혼합 사용 가능(*졍수 인데스가 앞이어야 함)

# 이스케이프 문자 : \n, \t
print("\n줄바꿈\n연습")
print("\\ reverse slash")
print(r"\n \t \\ 그대로 출력")  # r을 붙이면 그대로 출력 가능
print("글자가 '강조'되는 효과") # 문자 표현 시 "", '' 허용
print('글자가 "강조"되는 효과') # 문자 표현 시 "", '' 허용