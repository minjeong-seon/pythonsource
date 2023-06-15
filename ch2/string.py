# 파이썬 자료형
# 1. 문자열 :  '', "", ''' ''', """ """

# + : 문자열 결합
print("python "+"is easy to learn")

# * : 문자열 복제
print("python" * 3)

print("*" * 50)
print("내 프로젝트")
print("*" * 50)


# 인덱싱 : 문자열은 인덱스 값을 가지고 있음(0부터 시작)
str1 = "Life is too short"
print(str1[3])  # e <-- str1에서 4번째 자리 문자 출력


# 슬라이싱 [시작위치 : 끝위치] : 끝 위치는 포함하지 않음
print("str1[2:6]", str1[2:6])   # fe i  <-- 시작위치인 f부터 5번째 자리인 i까지 출력
print(str1[:6])     # Life i  <-- 시작위치 지정 안 하면 default = 0, 
print(str1[:])      # Life is too short <-- 아예 지정 안 하면 처음부터 끝까지 나옴
print(str1[:-4])    # Life is too s  <-- 음수는 오른쪽 끝에서 위치를 잡을 때 사용
print(str1[-5:])    # short


# len() : 문자열의 길이를 구하는 함수
print("str1 길이 : ", len(str1))


# 년도와 날씨를 구별해서 변수에 담기
str2 = "20230615Sunny"
date = str2[:8]
weather = str2[-5:]
print(date, weather)

# date 변수에 담긴 값을 년-월-일 순으로 다른 변수에 담기
year = date[:4]
month = date[4:6]
day = date[-2:]
print(year, month, day)


print()
# 주민등록번호 001205-3234567
# 남자(1,3) / 여자(2,4) 성별 출력
id_number = "001205-3234567"
gender = id_number[7]
if gender==1 or 3:
    print("남자")
else:
    print("여자")

if int(gender) % 2 == 1:
    print("남자")
else:
    print("여자")


str1 = "대한민국"
for s in str1:
    print(s, end="$")


print()
# 입력받은 숫자만큼(각 자릿수별로) 하트 출력
# num1 = input("숫자 입력: ")
# for i in range(len(num1)):
#     for j in range(int(num1[i])):
#         print("♥",end=" ")
#     print()
    


print("문자열 관련 함수")
# 문자열 관련 함수
# count() : 특정 문자 개수 반환
str1 = "forever"
print("str1에 포함된 알파벳 e의 개수 : ", str1.count("e"))


str1 = "python is best choice"



# find(찾는 문자, 시작위치, 끝위치) : 특정 문차 위치 반환 -- 끝위치는 포함 안 됨(시작위치는 포함)
print("str1에서 알파벳 i의 위치", str1.find("i"))
print("str1에서 알파벳 k의 위치", str1.find("k"))   # 찾는 문자가 존재하지 않으면 -1을 반환
print("str1에서 알파벳 i의 위치", str1.find("i", 8, 18))   # 찾기 시작할 위치를 지정 가능
print("str1에서 알파벳 i를 오른쪽에서부터 찾기", str1.rfind("i"))


# index() : find()와 기능은 동일하나, 없는 값 요청 시 ValueError 발생
print("찾는 문자의 시작 위치 반환", str1.index("b"))
#print("찾는 문자의 시작 위치 반환", str1.index("k"))    # ValueError: substring not found


# startWith() / endsWith() : 특정 문자로 시작하는지/끝나는지 True/False로 반환
print(str1.startswith("p"))
print(str1.endswith("p"))


# upper() / lower() : 문자열 대소문자 변환
print("대문자 ", str1.upper())
print("대문자 ", str1.lower())

# swapcase() : 대문자 -> 소문자, 소문자 -> 대문자로 변환
str1 = "Can I do this job?"
print(str1.swapcase())

print("abc" == "ABC")   # False : 대소문자 구별함


# lstrip(), rstrip(), strip() / :공백 제거 - 왼쪽, 오른쪽, 양쪽
str1 = "       look! **   "
print(str1)
print(str1.lstrip())    #        look! **/
print(str1.rstrip())    # /look! **
print(str1.strip())     # /look! **/


# replace() : 특정 문자열 변경
str1 = "Design is boring"
print("특정 문자열 변경", str1.replace("Design", "Pront"))  # Pront is boring


# split() => [](리스트)로 반환(공백마다)
print(str1.split())     # ['Design', 'is', 'boring']

a = "good"
print(a.split())        # ['good']

a = "g:O:o:d"
print(a.split(":"))     # ['g', 'O', 'o', 'd']

a = "하나\n둘\n셋"
print(a.splitlines())   # splitlines() : enter를 기준으로 나눔
print(a.split())    # enter도 공백 개념이므로 위와 결과 같음



# 문자열 구성 파악
# isdigit(), isalpha(), isalnum(), islower(), isupper()
print("12345".isdigit())    # True
print("abc123".isalpha())   # False
print("abc123".isalnum())   # True(알파벳/숫자로 구성되어 있는가)



# 사이트별 비밀번호를 만들어주는 프로그램
# http://www.naver.com

# 규칙 1 : http://www. 제외 => naver.com
# 규칙 2 : 처음 나오는 . 이후 부분은 제외 => naver
# 규칙 3 : 남은 문자 중 처음 3자리 + 문자 수 + 문자열 내 e의 개수 + ! 로 구성
# 완성된 비번 형태 : nav51!

site = "http://www.naver.com"
rule1 = site[11:]
rule2 = rule1[:rule1.find(".")]
password = rule2[:3]+str(len(rule2))+str(rule2.count("e"))+"!"
print("비밀번호 : ", password)