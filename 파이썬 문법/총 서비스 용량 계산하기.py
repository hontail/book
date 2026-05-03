KB = 1024 #용량 단위
total_service = 0

with open('access_log','r') as f: #access_log파일을 읽기 모드로 열기
    logs = f.readlines() #파일 전부를 리스트형태로 logs변수에 저장
    for log in logs: # 한 줄씩 꺼내기
        log = log.split() #단어별로 나눠서 다시 리스트 형태로 저장
        servicebyte = log[9] #10번째 단어는 servicebyte변수에 저장
        if servicebyte.isdigit(): #만약 10진로 이루어진 값이면 totoal_service 변수에 정수형태로 이어서 저장
            total_service += int(servicebyte)

total_service /= KB #총 더한 값을 KB단위로 나눠서 다시 저장
print("총 서비스 용량: %dKB" %total_service)
