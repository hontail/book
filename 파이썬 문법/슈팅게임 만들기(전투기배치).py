import pygame

BLACK = (0,0,0) #상수 검정 rbg값
pad_width = 480 #게임 화면 가로폭
pad_height = 640 #게임 화면 세로폭
fighter_width = 36 #전투기 가로폭
fighter_height = 38 #전투기 세로폭

def drawObject(obj,x,y): 
    global gamepad #전역변수 gamepad 접근
    gamepad.blit(obj,(x,y))  #obj를 x,y좌표에 그려라

def runGame():
    global gamepad, clock, fighter #전역변수 접근

    x = int(pad_width * 0.45) #x는 게임화면 0.45배
    y = int(pad_height * 0.9) #y는 게임화면 0.9배
    x_change = 0

    ongame = False #종료여부
    while not ongame: #동작할때까지 실행
        for event in pygame.event.get(): #발생한 이벤트들을 얻고 event변수에 저장
            if event.type == pygame.QUIT: #만약 저장한 이벤트가 종료면 종료
                ongame = True

            if event.type == pygame.KEYDOWN: #저장한 이벤트가 키입력이면 실행
                if event.key == pygame.K_LEFT: #방향키가 왼쪽이면 x축을 -5만큼 이동
                    x_change -= 5
                
                elif event.key == pygame.K_RIGHT: #방향키가 오른쪽이면 x축을 +5만큼 이동
                    x_change += 5 
            
            if event.type == pygame.KEYUP: #저장한 이벤트가 키를 떼는 거면 실행
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #만약 이벤트 키값이 왼쪽이거나 오른쪽이면 x는 0
                    x_change = 0
            
        gamepad.fill(BLACK) #게임패드를 검정으로 채우기

        x += x_change #현재위치에 이동한위치만큼 변화
        if x < 0: #0보다 작아지면 0고정
            x = 0
        elif x > pad_width - fighter_width: #x가 게임넓이 - 파이터 넓이보다 크면 값 저장
            x = pad_width - fighter_width

        drawObject(fighter,x,y) #figter오프젝트를 x,y축 좌표에 그려라)
        pygame.display.update() #실시간으로 위치 업데이트
        clock.tick(60) #1초당 60번 실행

    pygame.quit() #종료

def initGame():
    global gamepad, clock, fighter #게임패드, 시간, 파이터 전역변수 설정

    pygame.init() 
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('MyGalga')
    fighter = pygame.image.load('fighter.png') #파이터 변수는 fighter.pmg파일 이미지
    clock = pygame.time.Clock() #

initGame()
runGame()
