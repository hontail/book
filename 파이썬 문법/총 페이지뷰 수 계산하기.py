pageviews = 0

with open('acess_log','r') as f: #acces_log파일을 읽기 모드로 열기
    logs = f.readlines() #변수 logs에는 access_log 파일 1줄씩 나눠서 저장 
    for log in logs: #log변수에는 logs변수값 1줄씩 나눠서 저장
        log = log.split() #1줄을 다시 단어별로 나눠서 리스트형태로 저장
        status = log[8] #status변수는 8번째 인덱스 값 저장 즉 8번째 단어
        if status =='200': #만약 8번째 단어가 200이면 pageviews값에 +1저장
            pageviews += 1

print("총 페이지뷰:[%d]"%pageviews)
