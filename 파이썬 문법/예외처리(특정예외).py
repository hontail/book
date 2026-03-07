import time #time라이브러리 불러오기
count = 1 #count변수에 1 저장
try: #아래코드 실행
    while True: #아래 코드 반복
        print(count) #count 프린트 1출력
        count += 1 #카운트에 1 더해서 카운트에 저장
        time.sleep(0.5) #컴퓨터 0.5초간 정지 하고 다시 while문 맨 위로 이동

except KeyboardInterrupt: #Ctrl + c를 입력하면 아래코드 실행
    print('사용하제 의해 프로그램이 중단되었습니다.')
