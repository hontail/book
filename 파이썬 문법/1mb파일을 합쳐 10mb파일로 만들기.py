BUFSIZE = 256 * 1024 #한번에 저장할 버퍼크기
merge_filename = 'ret.exe'
filelist = ['python-3.5.2.exe_'+ str(x)for x in range(10)] #파일 + 문자열0부터 9까지 번호 매김

with open(merge_filename,'wb') as f: #ret.exe파일을 쓰기 모드로 열기
    for filename in filelist: #번호매긴 파일들을 1개씩 불러오기
        print("[%s]합치는 중.."%filename) #1번 반복할때마다 몇번째 파일 합치는지
        with open(filename, 'rb') as h: #파일을 열어서 읽기
            buf = h.read(BUFSIZE) #버퍼 크기만큼 변수 저장
            while buf: #읽을게 없을때까지 반복
                f.write(buf) #버퍼크기만큼 ret.exe파일에 쓰기
                buf = h.read(BUFSIZE) #다음 버퍼크기만큼 저장

print('파일 합치기가 완료되었습니다.')
