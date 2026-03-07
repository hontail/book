class Robot:
    def __init__(self, name):
        self.name = name #self를 써서 각 Robot클래스마다 고유한 이름을 저장

    def introduce(self):
        print(f"안녕, 내 이름은 {self.name}이야.") #slef.name을 통해 자신의 이름을 출력

robot1 = Robot("태권v") 
robot2 = Robot("마징가")

robot1.introduce()
robot2.introduce()
