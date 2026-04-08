f = open("stoctcode",'r') #stoctcode를 읽기 모드로 열어
h = open('stockcode_copy.txt', 'w') #stockcode_copy를 쓰기 모드로 열어

data = f.read() #data변수에 f파일을 저장
h.write(data) #data에 저장한 f파일을 h파일에 써

f.close()
h.close()
