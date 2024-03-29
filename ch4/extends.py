class Parent:
    def __init__(self) -> None:
        self.value = "테스트"
        print("Parent 클래스의 __init__ 호출")

    def test(self):
        print("Parent 클래스의 test 호출")

    def Child(Parent):
        def __init__(self) -> None:
            super().__init__()
            print("Child 클래스의 __inint__ 호출")


class Child(Parent):
    def __init__(self) -> None:
        super().__init__()  # 부모 클래스의 생성자 호출
        print("Child 클래스의 __inint__ 호출")


child = Child()
child.test()
print("부모의 value = {}".format(child.value))


class Car:
    speed = 0

    def upSpeed(self, value):
        """오버라이딩"""
        self.speed = self.speed + value

    def downSpeed(self, value):
        self.speed = self.speed - value


class SeDan(Car):
    seatNum = 0

    def upSpeed(self, value):
        """
        오버라이딩
        """
        self.speed = self.speed + value
        if self.speed > 150:
            self.speed = 150  # 최고 시속 150km로 제한
            print("현재 속도(자식 클래스) : %d" % self.speed)

    def getSeatNum(self):
        return self.seatNum


class Truck(Car):
    capacity = 0

    def getCapacity(self):
        return self.capacity


sedan1, truck1 = SeDan(), Truck()

sedan1.upSpeed(180)
# sedan1.downSpeed(20)
sedan1.seatNum = 5

truck1.upSpeed(150)
truck1.capacity = 100

print("승용차 속도 {}km, 좌석 수 {}개".format(sedan1.speed, sedan1.getSeatNum()))
print("트럭의 속도는 {}km, 용적량은 {}톤".format(truck1.speed, truck1.capacity))
