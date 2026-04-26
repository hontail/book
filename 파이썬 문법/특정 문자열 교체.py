t1 = input('찾을 단어를 입력하세요')
t2 = input('변경할 단어를 입력하세요')

with open('mydata.txt','r')as f: #1개는 읽기모드로 열고 다른 1개는 쓰기 모드로 열기
    with open('mydata2.txt','w') as h:
        text = f.read() #읽기모드 파일 전체를 저장
        text = text.replace(t1,t2) #읽기모드 파일의 단어를 찾고 변경할 단어로 변경
        h.write(text) #mydata2.txt파일에  덮어쓰기 저장

print('[%s]를 [%s]로 변경하였습니다.'%(t1,t2))
