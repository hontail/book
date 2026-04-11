import os

newfolder = input("새로 생성할 디렉터리 이름을 입력하세요") 
try:
    os.mkdir(newfolder) #newfolder이름의 디렉토리 생성ㅇ
    print(f"{newfolder}디렉터리를 생성합니다")
except Exception as e: #만약 오류갑 ㅏㄹ생하면 e에 넣고 출력
    print(e)
