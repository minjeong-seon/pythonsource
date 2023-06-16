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



# sort() : 리스트 원본 정렬
print("정렬 전 : ", numbers)
numbers.sort()
print("정렬 후 : ", numbers)

alpha = ["a","x", "e","b","c"]
alpha.sort()
print("sort() : ",alpha)

alpha = ["A","x","E","b","c","Z","X"]
alpha.sort()
print("sort() : ",alpha)    # ['A', 'E', 'X', 'Z', 'b', 'c', 'x']

kor = ["고양이", "개", "한글", "오렌지"]
kor.sort()
print(kor)   # ['개', '고양이', '오렌지', '한글']

mix = ["abc","한글","A","송아지"]
mix.sort()
print(mix)   # ['A', 'abc', '송아지', '한글']


# sort(reverse=True) : 내림차순 정렬
numbers = [273, 103, 5, 32, 65, 38, 9]
numbers.sort(reverse=True)  
print("reverse : ",numbers)      # [273, 103, 65, 38, 32, 9, 5]

kor.sort(reverse=True)
print("reverse : ",kor)



# index(찾을 요소) : 요소가 존재하면 위치 반환(없으면 에러 발생: value error)
print(kor[0])       # 한글
print(kor.index("한글"))        # 0



# insert(위치, 요소) : 지정한 위치에 입력한 요소 삽입
kor.insert(2, "악어")
print("insert() 후 : ", kor)        # ['한글', '오렌지', '악어', '고양이', '개']



# remove(삭제할 요소) : 요소 삭제(두 개 이상은 삭제 불가)
kor.remove("오렌지")
print("remove() 후 : ",kor)     # ['한글', '악어', '고양이', '개']



# pop() : 마지막 요소 꺼내기(삭제)
# pop(위치) : 지정한 위치의 요소 꺼내기(삭제) 
kor.pop()
print("pop() 후: ", kor)        # ['한글', '악어', '고양이']
element = kor.pop()
print("pop 요소 : ",element)
kor.pop(0)
print("pop() 후: ", kor)        # ['악어']



# count(찾을 요소) : 찾는 요소의 개수 반환
a = [1, 2, 3, 1]
print("a에 포함된 1의 개수 : ",a.count(1))      # 2



# clear() : 리스트 안 요소 전체 삭제
a.clear()
print("a clear() 후 : ",a)      # []


# 리스트 내용이 비어있는 경우 false 로 인식(문자열도 마찬가지)
listA = []
if listA:
    print("True")
else:
    print("False")

str = ""
if str:
    print("True")
else:
    print("False")



# in : 포함여부 확인
print("p" in "python")      # True

fruits = ["apple",'kiwi','melon','mango','grape']
print('kiwi' in fruits)         # True
print('melon' not in fruits)       # False



# 리스트 출력
for fruits in fruits:
    print(fruits, end=" ")      # apple kiwi melon mango grape
print()



# enumerate() : index 부여 (튜플 형태)
fruits2 = ["사과", "멜론", "딸기", "망고", "키위"]
for fruits2 in enumerate(fruits2):
    print(fruits2, end=" ")     # (0, '사과') (1, '멜론') (2, '딸기') (3, '망고') (4, '키위')
print()



# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# 70, 60, 55, 75, 95, 80, 85, 100, 88
# 중간고사 점수를 리스트로 생성하고, A 학급의 평균 구하기
score = [70, 60, 55, 75, 95, 80, 85, 100, 88]

total = 0
for num in score:
    total += num
print("A 학급 평균 : %.2f" % (total/len(score)))

# sum() : 합산 연산 함수 이용
print("A 학급 평균 : %.2f" % (sum(score)/len(score)))



# 1~20 리스트 생성 : [1,2,3,4,5,6,...]
list_B = list(range(1,21))
print(list_B)


# 비어있는 리스트에 1~ 101까지 숫자 채워넣기
list3 = []
for x in range(1,101):
    list3.append(x)
print(list3)

print()


# comprehension : 위에 for문과 같은 효과
list3 = [x for x in range(1,101)]
print(list3)

print()


# 리스트에서 '정'을 제외하고 출력
list4 = ["갑","을","병","정"]
for x in list4:
    if x != '정':
        print(x,end=" ")

# 위에꺼 comprehension
list5 = [x for x in list4 if x != '정']
print(list5)


# 1~100 까지의 숫자 중 홀수만 리스트로 생성
list_odd = [a for a in range(1,101,2)]
print(list_odd)


# 아래의 리스트에서 대문자만 추출해서 새로운 리스트로 생성 후 출력
list_mix = ['a','e','b','c','B','T','w','S']
list_upper = []
for x in list_mix:
    if x.isupper():
        list_upper.append(x)
print(list_upper)

# comprehension
list_bts = [x for x in list_mix if x.isupper()]
print(list_bts)


# [1,2,3,4] ==> [2,4,6,8]
print([x*2 for x in [1,2,3,4]])

# [0,1,2,3,4] ==> [0,1,4,9,16]
print([x*x for x in [0,1,2,3,4]])


# [1,2,3] ==> [[1,2,3],[2,3,4],[3,4,5]]
list_no = [1,2,3]
list_3 = []
for x in list_no:
    list_3.append([x, x+1, x+2])
print(list_3)

listC = [([x, x+1, x+2]) for x in list_no ]