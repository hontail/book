ch = input("문자를 1개 입력하세요:") #문자 1개 입력문
if len(ch) != 0: #만약 입력한 문자 길이가 0이 아니면 실행
    ch = ch[0] #ch에 리스트에 0을 넣어서 저장
    chv = ord(ch) #chv는 ch의 코드값 저장
    print(f"문자:{ch}\t 코드값: {chv}[{hex(chv)}]") #입력한 문자 ch, 코드값,아스키 코드 값 출력
