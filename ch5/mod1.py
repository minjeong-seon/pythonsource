def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# 모듈 함수 잘 돌아가는지 확인~
# __name__ 는 mod1을 실행 시 __main__ 이라는 이름을 가지게 됨
#    ==> 그러나 외부에서 mod1 실행 시 mod1 이라는 이름을 가지게 됨
if __name__ == "__main__":
    print(add(3, 4))
    print(sub(6, 4))
