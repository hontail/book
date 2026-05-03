visit_ip = [] #빈 리스트 생성

with open('access_log','r') as f: #acces_log 파일을 읽기 모드로 열기
    logs = f.readlines() #파일 전체를 리스트형태로 logs변수에 저장
    for log in logs: #리스트에서 한줄씩 꺼내기
        log = log.split() #단어별로 나눠서 다시 리스트로 저장
        ip = log[0] #ip는 첫번째 단어 저장
        if ip not in visit_ip: #visit_ip 리스트에 첫번째 단어가 없으면 추가
            visit_ip.append(ip)

print("고유 방문자 수:[%d]"%len(visit_ip)) #추가된 길이만큼 고유 방문자 수가 됨
