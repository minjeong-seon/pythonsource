# 파이썬 자료형
# 3. 튜플 (리스트와 거의 유사함) : 여러 개의 자료를 하나의 변수로 관리할 때 사용
# () 사용, 수정/삭제 불가, 읽기만 가능
# 자료 읽기는 리스트보다 빠름

t1 = 1,2,3
print(t1)       # (1, 2, 3)

# 원소 개수가 하나라면 ','가 필요함
t2 = (1,)
print(t2)       # (1,)

t3 = (1,2,("class","holiday"))
print(t3)       # (1, 2, ('class', 'holiday'))


# 요소 삭제 불가 : 'tuple' object doesn't support item deletion
# 요소 변경 불가 : 'tuple' object does not support item assignment


# 인덱싱 / 슬라이싱
print(t1[0])        # 1
print(t1[0:2])      # (1, 2)


# 함수 리턴 값 ==> 여러 개의 값이 가능함 ==> 튜플로 리턴

# 튜플 ==> 리스트
print(list(t1))     # [1, 2, 3]

# 리스트 ==> 튜플
list1 = [1,2,3,4]
print(tuple(list1))     # (1, 2, 3, 4)