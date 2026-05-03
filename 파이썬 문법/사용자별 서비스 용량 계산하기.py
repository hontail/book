services = {} #빈 딕셔너리 생성

with open('access_log','r') as f: #access_log파일을 읽기 모드로 열기
    logs = f.readlines() #모든 내용을 logs변수에 저장
    for log in logs: #1줄씩 꺼내서 반복
        log = log.split() #단어별로 나눠서 리스트에 저장
        ip = log[0] #첫 번째 단어는 ip
        servicebyte = log[9] #10번째 단어는 서비스바이트
        if servicebyte.isdigit(): #만약 서비스바이트가 10진수로이뤄진 정수로만 돼 있으면 정수형으로 다시 저장
            servicebyte = int(servicebyte)
        else: #그렇지 않으면 서비스바이트는 0
            servicebyte = 0

        if ip not in services:   #딕셔너리에 ip가 없다면 ip를 키로 서비스 바이트를 값으로 저장
            services[ip] = servicebyte
        else:
            services[ip] += servicebyte #ip가 딕셔너리에 있으면 ip값에 서비스바이트값을 추가해서 저장

ret = sorted(services.items(), key=lambda x: x[1], reverse=True) #튜플 형태(서비스용량을 기준으로)정렬 원본은 그대로 (x[0]은 ip,키값) (x[1]은 용량,value)

print("사용자IP - 서비스용량") 
for ip, b in ret: #ip,b변수에 키값, 값 나눠서 저장
    print("[%s]-[%d]"%(ip,b)) 
