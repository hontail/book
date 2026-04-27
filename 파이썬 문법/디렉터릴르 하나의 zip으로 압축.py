from zipfile import *
import os

def compressAll(zipname,folder): #zipname,folder를 파라매터로 받는 함수
    print('[%s]->[%s]압축...'%(folder, zipname)) #압축과정 출력
    with ZipFile(zipname, 'w') as ziph: #zipname파일을 쓰기모드로 열기
        for dirname, subdirs, files in os.walk(folder): #현재디렉토리 이름, 내부디렉토리, 파일들 저장
            for file in files: #파일을 1개씩 불러와서 zipname파일에 현재디렉토리 이름,파일명을 연결해서 저장
                ziph.write(os.path.join(dirname,file))

folder = 'tmp' #tmp폴더
zipname = folder + '.zip' #tmp폴더 .zip으로 다시 이름 짓기
compressAll(zipname, folder) 
