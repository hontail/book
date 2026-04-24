def getTextFreq(filename): #filename파라매터를 받는 함수
    with open(filename, 'r')as f: #파라매터를 읽기 모드로 엶 f이름으로 사용
        text = f.read() #filename을 text변수에 저장
        fa = {} #빈 딕셔너리 생성
        for c in text: #파라매터만큼 반복에서 c에 저장
            if c in fa: #c가 딕셔너리 안에 있으면 
                fa[c] += 1
            else:
                fa[c] = 1
    return fa

ret = getTextFreq('mydata.txt') #getTextFreq 실행값을 ret에 저장
ret = sorted(ret.items(),key=lambda x:x[1], reverse=True) #실행값을 내림차순으로 정렬원본도 바꿈
for c, freq in ret:
    if c == '\n':
        continue
    print("[%c] => [%d]회 나타남" %(c,freq))
