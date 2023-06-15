# 반복문
# while, for

# 1~10 출력

i = 1
while i < 11:
    print(i, end="")
    i += 1

print()

# 1~100까지의 수 중에서 짝수만 출력
i = 2
while i <= 100:
    if i%2 ==0:
        print(i, end=" ")
    i +=1

print()


# 구구단 3단 출력
# 파이썬에서는 i++ 사용 불가
i = 1
while i < 10:
    print("{} * {} = {}".format(3, i, 3*i))
    i += 1


# range(시작값, 종료값, 증감값) : 범위 지정
print(range(7))     # range(0, 7) => 0~6 까지의 수
print(list(range(1,8)))     # [1, 2, 3, 4, 5, 6, 7]
print(list(range(0,12,2)))  # [0, 2, 4, 6, 8, 10]


# in : 포함
# not in : 미포함
print("in 기호")
print("y" in "python")  # True : python 문자열 안에 y가 포함되어 있으므로 True



# for
for i in range(10):
    print(i, end=" ")

print()



# 사용자로부터 숫자 입력 받아서 1~입력한 숫자까지 합계 구한 후 출력

# no = int(input("숫자 입력 : "))
# result = 0
# for i in range(1, no + 1):
#     sum += i
# print("1 ~ {}까지의 합 : {}".format(no, result))


# sum() : for문 쓰지 않아도 범위 값의 합계 구할 수 있음
print("sum() 함수 : ")
print(sum(range(1, 11)))



# 큰수 ~ 작은수 순으로 반복문 돌릴 때
for i in range(10, -1, -1):
    print(i, end=" ")

print()


# 이중 for 문
# i 5회 반복 + j가 실행구문을 5회 반복할 때까지
for i in range(5):
    for j in range(5):
        print(i+j, end=" ")
    print()


# 구구단 2~9단 출력
for i in range(2,10):
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,i*j), end="\t")
    print()


# break, continue : 자바 개념과 동일
i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1