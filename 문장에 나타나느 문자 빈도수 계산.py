def getTextFreq(filename): #filename파라매터를 받는 함수
    with open(filename, 'r')as f: #파라매터를 읽기 모드로 엶 f이름으로 사용
        text = f.read() #파라매터 filename의 내용을 문자로 text변수에 저장
        fa = {} #빈 딕셔너리 생성 
        for c in text: #filename의 내용을 1개씩 꺼내서 c에 저장
            if c in fa: #c가 딕셔너리 안에 있으면 값에 +1을 해서 저장
                fa[c] += 1 
            else: #딕셔너리 안에 없으면 값은 1 
                fa[c] = 1
    return fa #모든 문자에 대한 횟수가 저장됨

#예를들어 apple이 있으면 a는 빈 딕셔너리에 없으니 'a' :1 로 저장 2번째 p는 'p':1 이 있으니 +1을 해서 'p':2로 저장


ret = getTextFreq('mydata.txt') #getTextFreq 실행값을 ret에 저장
ret = sorted(ret.items(),key=lambda x:x[1], reverse=True) #원본은 그대로 복사본을 만들어서 정렬 
for c, freq in ret:
    if c == '\n':
        continue
    print("[%c] => [%d]회 나타남" %(c,freq))
