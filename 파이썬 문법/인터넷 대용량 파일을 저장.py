from urllib.request import urlopen

BUFSIZE = 256*1024 #한번에 저장할 바이트 파일 크기

fileurl = 'https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe'
filename = fileurl.split('/')[-1] #마지막/ 파이썬 exe파일 이름을 저장
try:
    with urlopen(fileurl) as f: #url을 열어서 바이트데이터 받기
        with open(filename,'wb') as h: #저장한 파일명의 파일 생성
            buf = f.read(BUFSIZE) #저장할 바이트크기 만큼 변수에 저장
            while buf: #파일에 받은 바이트크기 만큼 쓰기 만약 받을 바이트 크기가 0이 되면 종료
                h.write(buf)
                buf = f.read(BUFSIZE) #다시 저장할 바이트 크기 만큼 받기
except Exception as e: #예외 처리
    print(e)
