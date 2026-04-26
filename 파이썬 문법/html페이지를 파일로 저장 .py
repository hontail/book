from urllib.request import urlopen

url = 'https://www.python.org/' #접속할 사이트 주소 저장
with urlopen(url) as f: #접속할 사이트 주소에 데이터를 요청 
    doc = f.read().decode() #받은 바이트 데이터를 문자열로 변환해서 저장
    with open('pythonhome.html','w') as h: #pythonhome파일을 쓰기모드로 열기
        h.writelines(doc) #파일에 문자열로 변환한 데이터를 저장
