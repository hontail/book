from time import localtime

t = localtime() #대한민국 날짜 저장
start_day = '%d-01-01'%t.tm_year #올 해 년도 1월 1일 start_day에 저장
elapsed_day = t.tm_yday # 올해 n번쨰의 날짜 정보를 elapsed_day에 저장

print(f'오늘은 {start_day}이후 {elapsed_day}일째 되는 날입니다')
