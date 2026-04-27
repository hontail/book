from zipfile import * #zipfile모듈 모든 함수 불러오기

def compressZip(zipname, filename): #zip이름 file이름 파라매터로 받는 함수
    print('[%s]->[%s]압축...'%(filename,zipname)) #압축되고 있다는 메시지출력
    with ZipFile(zipname,'w') as ziph: #zipname파일을 쓰기로 열기
        ziph.write(filename) #파일이름 쓰기

    print('압축이 끝났습니다.')

filename = 'mydata.txt' #파일명 변수
zipname = filename + '.zip' #집파일명으로 다시 저장
compressZip(zipname, filename) 
