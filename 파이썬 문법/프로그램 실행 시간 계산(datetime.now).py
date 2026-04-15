from datetime import datetime

start = datetime.now() #현재 시간 년도,월,일,시간,분초 저장
print("1에서 백만까지 더합니다")
ret = 0 
for i in range(1000001): #백만번 반복
    ret += i #백만까지 다 더하면서 증가
print(f'1에서 백만까지 더한 결과 : {ret}') #ret에 백만까지 누적 값 출력
end = datetime.now() #현재 시간 년도,월,일 시간 분초 저장
elapsed = end - start #elapsed변수는 end 시간 - start시간 즉 걸린 시간
print('총 계산 시간', end='');print(elapsed) 
elapsed_ms = int(elapsed.total_seconds()*1000) #총 걸린 시간을 ms초 단위로 출력
print(f'총 세간시간: {elapsed_ms}')
