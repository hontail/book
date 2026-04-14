import os #파일 접근 라이브러리
from os.path import exists #os.path에 exists함수 활용

dir_name = input("새로 생성할 디렉터리 이름을 입력하세요") #생성할 디렉터리 이름을 dir_name변수에 저장
if not exists(dir_name): #만약 새로 생성할 디렉터리 이름이 존재하지 않으면
    os.mkdir(dir_name) #디렉터리 이름에 디렉터리를 생성
    print(f"{dir_name}디렉터리를 생성합니다")
else:
    print(f"{dir_name}은 이미 존재합니다")
