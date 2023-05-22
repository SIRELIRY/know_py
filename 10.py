# 객체지향
# 객체와 객체 사이의 상호작용으로 프로그램을 구성하는 프로그래밍 패러다임
# 프로그램을 유연하고 변경을 쉽게 만들어 대규모 소프트웨어 개발에 사용

# /객체지향 패러다임의 특징
# -추상화 : 공토으이 속성이나 기능을 도출
# -캡슐화 : 데이터 구조와 데이터의 연산을 결합
# -상속 : 상위 개념의 특징이 하위 개념에 전달
# -다형성 : 유사 객체의 사용서을 그대로 유지
# 클래스와 인스턴트
# 객체지향의 활용

# 공통적인 기능을 만든 후 추가적 기능을 만들면 관리,개발이 편리하다

# class 클래스 이름 :
#     초기자 정의
#     메소드 정의

# [메소드의 정의]
# (구문형식)
# class 클래스 이름:
#     def 메소드 이름(self,매개변수 리스트):
#         코드 블럭

# (self 매개변수)
# -모든 메소드의 첫번째 매개변수
# -메소드의 구현에 사용되지만 메소드 호출 시 사용되지 않음
# -객체 자신을 참조하여 클래스 정의에 포함된 멤버에 접근 시 사용

# class first name is U
class Cone:
    def __init__(self, radius=20, height=30):
        self.r = redius
        self.h - height

    def get_vol(self):
        return 1/3 * 3.14 * self.r ** 2 * self.h

    def get_surf(self):
        return 3.14 * self.r ** 2 + 3.14 * self.r * self.h

# self.~ 를 사용하지 않으면 def안에서 쓰인 변수를 클래스 안의 다른 def안에서 사용할수 없기 때문에 사용함


class BMI:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_BMI(self):
        return self.weight / (self.height / 100) ** 2

    def get_status(self):
        BMI = self.get_BMI()

        if BMI() >= 25:
            return "비만"
        elif BMI >= 23 and BMI < 25:
            return "과체중"
        elif BMI >= 18.5 and BMI < 23:
            return "정상"
        else:
            return "저체중"
