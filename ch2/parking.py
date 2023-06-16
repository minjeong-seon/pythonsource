# ord() : ASKII CODE 값 반환해줌
# chr() : ASKII CODE를 알파벳으로 반환해줌

print(ord("A"))     # 65
print(chr(65))      # A




## 실습 - 주차장 프로그램 작성
# 조건1 : [1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료
# 조건2 : 메뉴 선택 받기
# 조건3 : 1번 선택 시 리스트에 알파벳 대문자 순서대로 추가(5대 까지만 가능) (--> append() 리스트 뒤에 요소 추가)
#         자동차 다 빼고 나면 '주차장 비어있음'
#         3번 누르면 프로그램종료


parking_lot = []            # 주차장 리스트
top, car_name = 0, "A"      # 주차위치, 자동차 이름

print("=========================================")

while True:
    print("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료")
    no = int(input("메뉴 선택 : "))

    if no <= 3:
        if no == 1:
            if top >= 5:
                print("주차장이 꽉 찼습니다.")
            else:
                parking_lot.append(car_name)
                print("{} 자동차 들어감. 주차장 상태 ==> {}".format(car_name,parking_lot))
                
                top += 1
                car_name = chr(ord(car_name) + 1)
        elif no == 2:
            if top == 0:
                print("주차장이 비어있습니다.")
            else:
                leave_car = parking_lot.pop()
                print("{} 자동차 나감. 주차장 상태 ==> {}".format(leave_car, parking_lot))

                top -= 1
                car_name = chr(ord(car_name) - 1)
        else:
            print("프로그램 종료")
            break
        print("=========================================")
    else:
        print("번호를 확인해 주세요.")

