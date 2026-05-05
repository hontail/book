import pygame #pygame모듈 불러오기

#게임에 사용되는 전역변수 정의
BLACK = (0,0,0) #3가지 값을 튜플로 받는 상수 
pad_width = 480 #폭 480
pad_height = 640 #높이 640

#게임 실행 메인 함수
def runGame(): #게임 실행 함수
    global gamepad, clock #gamepad, clock변수 생성 전역변수

    doneFlag = False #실행 종료 조건문
    while not doneFlag: #True가 될때까지 반복
        for event in pygame.event.get(): #이벤트 발생하면 event에 저장
            if event.type == pygame.QUIT: #만약 저장한 이벤트가 종료면 True값 저장
                doneFlag = True
        

        #게임 화면을 검은색으로 채우고 화면을 업데이트 함
        gamepad.fill(BLACK) #
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

#게임 초기화 함수
def initGame(): 
    global gamepad, clock #전역 변수 gamepad, clock 선언

    pygame.init() #
    gamepad = pygame.display.set_mode((pad_width, pad_height)) #가로 세로에 저장한 값 만큼 게임패드 생성
    pygame.display.set_caption('MyGalaga') #상단 이름 설정
    clock = pygame.time.Clock() 

initGame()
runGame()
