# 모듈에 대하여 배워볼 것이다
# import를 통해 다른 사람이 만든 코드를 쉽게 가저올수 았다 -> 이때 import 해서 가저올수 있는 것이 모듈이다.
# 모듈이란 : 함수, 상수 또는 클래스를 모아 놓은 집합체 이다.
# 모듈: 클래스, 함수, 상수의 집합 / 패키지: 하위 패키지 및 모듈의 집합 -> 페키지가 모였을때. 라이브러리라고 함
# 1) 모듈 등록 방식 : 구문형식 ex) import모듈이름[as별칭] -> 파이썬 모듈을 프로그램 내부에서 사용할 수 있게 네임스페이스에 추가하는 명령어이다.
# 이때 멤버 접근 연산자(.)를 이용한다 ex)점 표기법 as.메서드 ) if as=m { m.메서드}
# 2) 모듈 등록 방식 : 구문형식 ex)from모듈이름import메소드1,[메소드/함수/클래스...]
# from모듈이름import* 이때 장점) 모듈이름 없이 변수, 함수, 클래스를 사용할수 있음
# dir 함수 : 네임스페이스에 등록되어 있는 모든 이름들을 리스트로 반환함
# help 함수 : 대화형 도움말 시스템 호출 또는 클래스나 메소드의 사용방법 반환함 ex01)help(math.abs) ex02) help("python".upper)

# 특정 객체를 이름에 따라 구분할 수 있는 범위
# 지역NS: 함수 또는 메소드 내의 이름 공간
# 전역NS: 모듈 전체에서 통용되는 이름 공간
# 빌트인NS: 모든 코드 범위에서 통용되는 이름 공간

# 모듈의 제거 : del 등록된 모듈이름 -> 네임스페이스 내 모듈의 멤버 식별자 제거함 (잘 사용되지 않지만 모듈을 임포트 후 오류가 발생한다면..)

# math 모듈을 활용한 원뿔 계산
# --------------------------

# 원뿔 클래스 정의
import math

print(math.pi)


class Cone:
    def __init__(self, radius=20, height=30):
        self.r = radius
        self.h = height

    def get_vol(self):
        return 1/3 * math.pi * self.r ** 2 * self.h

    def get_surf(self):
        return math.pi * self.r ** 2 + math.pi * self.r * self.h
est