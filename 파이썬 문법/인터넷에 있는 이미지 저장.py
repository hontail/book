from urllib.request import urlopen

imgurl = 'http://www.iaidol.com/img_sample.jpg' #인터넷 이미지 주소
imgname = imgurl.split('/')[-1] #/를 기준으로 나눠서 imgname에 저장 하는데 맨 마지막 거만 저장 즉 파일명만 추출
try:
    with urlopen(imgurl) as f: #imgurl을 열어서 데이터 받아
        with open(imgname, 'wb') as h: #imgname에는 바이트를 적을거야
            img = f.read() #img변수에는 url을 요청해서 받은 바이트 데이터를 저장하고
            h.write(img) #받은 바이트 데이터를 imgname변수에 덮어씌울거야
except Exception as e: #예외 상황이 생기면 오류 메시지 출력
    print(e)
