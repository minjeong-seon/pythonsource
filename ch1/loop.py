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


