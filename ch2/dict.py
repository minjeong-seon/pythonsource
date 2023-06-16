# 파이썬 자료형
# 4. dictionary (자바의 Map과 동일함 : key, value)
# {} 사용

# *key 값은 str, int 가능
# *value 값은 str, int, list, tuple, dictionary 가능


dict1 = {"name": "kim", "age": 23}
print(dict1)        # {'name': 'kim', 'age': 23}

# 특정 key에 해당하는 value 출력
print(dict1["name"])       # kim
print(dict1["age"])         # 23
#print(dict1["addr"])    # 없는 key 값 호출 시 ==> KeyError: 'addr'
#에러 발생 시 try exception 처리가 필요함

dict2 = {0:"Hello Pyhon", 1:"Hello Java"}
print(dict2[0])     # Hello Pyhon

dict3 = {"arr": [1,2,3,4]}
print(dict3["arr"])     # [1, 2, 3, 4]



# dictionary에 요소 추가
dict1["birth"] = "0613"
print(dict1)        # {'name': 'kim', 'age': 23, 'birth': '0613'}

dict2[2] = ["Hello Spring", "Hello Javascript"]
print(dict2)        # {0: 'Hello Pyhon', 1: 'Hello Java', 2: ['Hello Spring', 'Hello Javascript']}

dict3["rank"] = (17,18,19,20)
print(dict3)        # {'arr': [1, 2, 3, 4], 'rank': (17, 18, 19, 20)}


# 각 숫자가 몇 개씩 나오는지 구하여 딕셔너리 생성
# {1: 몇 개, 2: 몇 개....}
numbers = [1,2,3,1,2,5,4,3,5,4,6,5,7,2,8,7,3]

counter = {}
for number in numbers:
    counter[number] = numbers.count(number)
print(counter)      # {1: 2, 2: 3, 3: 3, 5: 3, 4: 2, 6: 1, 7: 2, 8: 1}



# 특정 key 값 삭제 : del 딕셔너리 이름[삭제할 key값] 사용
del dict1["birth"]
print(dict1)        # {'name': 'kim', 'age': 23}



# 함수
# get(key 값) : 없는 값을 요청해도 에러 발생 x ==> 딕셔너리 값 호출 시 get 을 사용 하는 이유!(==안전함)
print(dict1.get("name"))    # kim
print(dict1.get("addr"))    # None : 없는 key 값은 None을 반환