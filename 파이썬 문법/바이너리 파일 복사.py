bufsize = 1024 #데이터를 담을 크기 1024
f = open("img_sample.jpg", 'rb') #rb는 바이너리 즉 2진수 형태로 읽을거야, 텍스트가 아니라 파일을 읽을 때 사용
h = open("img_sample_copt.jpg", 'Wb')

data = f.read(bufsize) #data에 bufsize크기만큼 f변수를 읽어서 저장할거야
while data: #data값이 있을때만 반복
    h.write(data) #h에 data에 값을 적어
    data = f.read(bufsize) #data에 변수 f를 또 busize만큼 읽읅어야

f.close()
h.close()
