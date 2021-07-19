#1.4 클래스(class)
"""
-규약, 틀
-class&object(객체,인스턴스)
-구조
    :명사
        attribute,property,instance 변수
    :동사
        method
-유형
    :파이썬이 기본적으로 제공하는 클래스
    :User defined 클래스
"""
#------------------------------------------------------------------------
#1.4.1 클래스 정의/클래스 호출(=객체 만들기)
class SoccerPlayer:

    def shoot(self):
        print("슛을 날립니다")
        print("슈웃~")

    def pass_the_ball(self):
        print("패스를 합니다")

player=SoccerPlayer()
print(player)

player.shoot()
player.pass_the_ball()

player1=SoccerPlayer()
player2=SoccerPlayer()

player1.shoot()
player2.shoot()

#------------------------------------------------------------------------

#1.4.1.2 attribute 초기화(feat.생성자)
class SoccerPlayer:
    def __init__(self):
        print("나 태어났어")

    def shoot(self):
        print("슛을 때립니다")

player1=SoccerPlayer()

class SoccerPlayer:
    def __init__(self,height,weight):
        print("나 태어났어")
        self.wow_height=height
        self.wow_weight=weight

    def shoot(self):
        print("슛을 때립니다")

player1=SoccerPlayer(height=180,weight=50)
print(player1.wow_height)
print(player1.wow_weight)

player2=SoccerPlayer(height=160,weight=40)
print(player2.wow_height)
print(player2.wow_weight)

#self의 존재 이유
class SoccerPlayer:
    def __init__(self,height,weight):
        print("나 태어났어")
        self.wow_height=height
        self.wow_weight=weight

    def shoot(self):
        self.wow_height=self.wow_height+1
        print("슛을 때립니다")

player1=SoccerPlayer(180,70)
print(player1.wow_height)
player1.shoot()
print(player1.wow_height)
#------------------------------------------------------------------------

#1.4.2 상속(inheritence)
class Human:
    def __init__(self,wow_weight,wow_height):
        self.weight=wow_weight
        self.height=wow_height

    def walk(self):
        print("걷습니다")

h1=Human(60,170)
h1.walk()

class Athelte(Human):
    """
    def __init__(self,wow_weight,wow_height):
        self.weight=wow_weight
        self.height=wow_height

    def walk(self):
        print("걷습니다")
    """
    def workout(self):
        print("운동을합니다")

h2=Athelte(50,160)
h2.walk()

class Athlete(Human):
    def __init__(self,wow_weight,wow_height,fat_rate):
        super().__init__(wow_weight,wow_height)
        self.fat_rate=fat_rate
        
    def workout(self):
        print("운동을합니다")

h3=Athlete(50,180,11)
h3.walk()
h3.workout()

class SoccerPlayer(Athlete):

    def workout(self):
        print("축구를한다")

h4=SoccerPlayer(50,180,11)
h4.walk()
h4.workout()
#------------------------------------------------------------------------

#1.4.3 파이썬 기본 자료형(클래스)별 api 살펴보기
#API(Application Programming Interface)
#프로그래밍 언어, 라이브러리, 어플리케이션 등이 제공하는 기능들을 제어할 수 있게 만든 인터페이스
a=[1,2,3]
c={}

a=[1,2,3]
#a=list([1,2,3])
#a=className()
a.append(3)
print(a)

c={"c":123,"d":1234}
print(c.keys())

#------------------------------------------------------------------------

#1.4.4 객체를 인스턴스(instance) 변수로 가지고 있기
class SoccerPlayer:
    def __init__(self,weight):
        self.weight=weight
        
a=SoccerPlayer(10)
print(a.weight)

"""
class SoccerPlayer:
    def __init__(self,historical_weight_list):
        self.historical_weight_list=historical_weight_list

player1=SoccerPlayer([100,90,95,80])
"""

class SoccerCoach:
    def __init__(self, num_carrer_year):
        self.num_carrer_year=num_carrer_year
class Team:
    def __init__(self,coach,player_list):
        self.coach=coach
        self,player_list=player_list

player1=SoccerPlayer(70)
player1=SoccerPlayer(80)

coach=SoccerCoach(10)

team=Team(coach=coach, player_list=[player1,player2])
team.coach.num_career_year
#------------------------------------------------------------------------


#------------------------------------------------------------------------
