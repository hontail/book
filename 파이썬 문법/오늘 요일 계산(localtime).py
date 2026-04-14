from time import localtime

weekdays = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일'] #출력할 요일 weekdays변수에 저장

t = localtime() #현재 대한민국 날짜 변수 t에 저장
today = '%d-%d-%d' %(t.tm_year, t.tm_mon, t.tm_mday) #년,월,일 정보를 today변수에 ㅓ장
week = weekdays[t.tm_wday] #현재 대한민국 날짜에 요일정보를 0이면 월요일 정수값을 받아서 리턴 weekdays[정수] = 요일 저장

print(f"{today}오늘은{week}입니다")
