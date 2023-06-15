# 파이썬 자료형
# 2. list 리스트
# []


# 리스트 생성
list1 = []
list2 = ['a',1,3.15,True]
print(list1)
print(list2)
list3 = [['a',1,3.15,True], 'b', 35, 45]
print(list3)


# 리스트 인덱싱
print(list2[0])     # a
print(list2[2])     # 3.15 
print(list2[-1])    # True
print(list3[0])     # ['a', 1, 3.15, True]
print(list3[0][1])  # 1 <-- 2차원 배열의 [1]을 가져옴 


# 리스트 슬라이싱
print(list2[0:2])   # ['a', 1]
print(list3[0:2])   # [['a', 1, 3.15, True], 'b']
print(list3[:-3])   # [['a', 1, 3.15, True]]
print(list3[0][:3]) # ['a', 1, 3.15] <-- list3[0] 안의 [:3] 슬라이싱


# 2차원 리스트에서 특정 요소만 출력
list4 = [1, 2, ['a', 'b', ['Life', 'is']]]
print(list4[2][2][1])
print(list4[-1][-1][-1])


# + : 연결
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)  # [1, 2, 3, 4, 5, 6]
print(a[0] + b[1])  # 6 --> 산술연산됨


# * : 복제 
print(a*3)      # [1, 2, 3, 1, 2, 3, 1, 2, 3]


# 리스트 특정 요소 수정
a[1] = 7
print(a)    # [1, 7, 3]

a[2] = "Life"
print(a)    # [1, 7, 'Life']

b[1:2] = [10,11]
print(b)    # [4, 10, 11, 6] : b[1:2] = 5인데 5대신 10, 11이 요소로 들어감

b[1] = [15, 16, 17]
print(b)    # [4, [15, 16, 17], 11, 6] : 인덱스 위치에 바로 넣으면 2차원 리스트가 됨


# 리스트 요소 삭제
del b[1]
print(b)    # [4, 11, 6]

b[0:1] = []
print(b)    # [11, 6]


numbers = [230, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number >= 100:
        print("100 이상의 수 ", number)


# 리스트 요소의 자릿수 출력하기
# ex) 273 은 3자릿수입니다.
for number in numbers:
    print("{}는 {}자릿수입니다.".format(number, len(str(number))))


list4 = list([1,2,3])   # 에러발생 방지용 []
print(list4)


# append() : 리스트 뒤에 요소 추가
list4.append(5)
print(list4)        # [1, 2, 3, 5]
list4.append([6, 7, 8])
print(list4)        # [1, 2, 3, 5, [6, 7, 8]]


# () : 튜플 (여러 개의 자료를 하나의 변수로 관리할 때 사용)