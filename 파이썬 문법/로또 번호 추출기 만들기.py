from random import shuffle #모듈에서 shuflle,sleep함수만 가져옴
from time import sleep

gamenum = input("로또 게임 회수를 입력하세요:") #문자열로 저장

for i in range(int(gamenum)): #문자열을 정수형으로 변환, 반복
    balls = [x+1 for x in range(45)] #리스트에 0부터 44까지 +1을 해서 저장 1,2,3,4,5~45까지
    ret = [] #빈 리스트
    for j in range(6): #6번 반복
        shuffle(balls) #리스트안의 값들을 섞는 함수
        number = balls.pop() #맨 위의 값을 꺼낸
        ret.append(number) #빈 리스트에 맨 위의 값을 추가
    ret.sort() #리스트 원본을 정렬
    print("로또 번호[%d]:"%(i+1),end='') #게임 회수만큼 로또 번호 매김
    print(ret)
    sleep(1) #1초 대기시간
