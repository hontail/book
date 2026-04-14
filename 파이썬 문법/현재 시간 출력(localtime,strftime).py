from time import localtime, strftime 

logfile = 'test_log' #logfile변수에 test_log문장 저장
def writelog(logfile, log): #writelog함수는 logfile, log를 파라매터로 받고
    time_stamp = strftime('%Y-%m-%d %X\t',localtime()) #time_stamp변수는 시간을 년,월,일,시간으로 저장
    log = time_stamp + log + '\n' #log변수에 time_stamp변수값을 1개씩 출력하고 줄바꿈해서 다시 저장 X
                                    #log변수에 시간, 밑에 첫 번째 로깅 메시지 + 줄바꿈

    with open(logfile, 'a') as f: #logfile을 추가로 적는 기능으로 열기를 f로 이름 정함
        f.writelines(log) #logfile에 줄바꿈한 것들(log)를 파일의 마지막에 적기

writelog(logfile, '첫 번째 로깅 문장입니다.')  #함수 실행 
