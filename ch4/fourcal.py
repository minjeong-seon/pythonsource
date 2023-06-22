class FourCal:
    """
    사칙연산 메소드를 가지고 있는 클래스 작성
    """

    def __init__(self, num1, num2) -> None:
        """
        두 개의 변수를 받아서 멤버 변수(num1, num2) 초기화
        """
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """두 개의 멤버변수 합산 결과 리턴"""
        return "{} + {} = {}".format(self.num1, self.num2, self.num1 + self.num2)

    def sub(self):
        """두 개의 멤버변수 감산 결과 리턴"""
        return "{} - {} = {}".format(self.num1, self.num2, self.num1 - self.num2)

    def mul(self):
        """두 개의 멤버변수 곱셈 결과 리턴"""
        return "{} * {} = {}".format(self.num1, self.num2, self.num1 * self.num2)

    def div(self):
        """두 개의 멤버변수 나누기 결과 리턴"""
        return "{} / {} = {}".format(self.num1, self.num2, self.num1 / self.num2)


# 객체 생성
result = FourCal(int(input("num1 : ")), int(input("num2 : ")))

# 함수 호출
print(result.add())
print(result.sub())
print(result.mul())
print(result.div())
