import os #파일 접근 라이브러리 사용
from os.path import exists,isdir,isfile #os.path 모듈의 파일이 존재,디렉터리인지,파일인지 찾는 함수사용

files = os.listdir() #files변수에 디렉터리에 있는 모든파일을 리스트형태로 생성
for file in files: #files리스트에 있는 파일들을 1개씩 꺼내서 file변수에 저장반복
    if isdir(file): #만약 1개씩 꺼낸 file이 디렉터리면
        print(f"DIR: {file}") #DIR :파일이름
        
for file in files: 
    if isfile(file): #만약 파일이면
        print(f"FILE:{file}") #FILE : 파일이름

