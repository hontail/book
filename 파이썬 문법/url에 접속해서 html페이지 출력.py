from urllib.request import urlopen

url = 'https://www.python.org' #접속할주소 저장
with urlopen(url) as f: #주소에 데이터를 요청해서 받기
    doc = f.read().decode() #주소데이터를 2진수로 읽고 문자열로 디코딩 
    print(doc)
