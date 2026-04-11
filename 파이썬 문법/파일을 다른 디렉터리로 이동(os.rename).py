from os import rename #os라이브러리접근 rename함수꺼내오기

target_file = 'stockcode.txt'  #stockcode텍스트 파일을 target_file에 넣기
newpath = input(f"{target_file}을 이동할 디렉터리의 절대경로를 입력하세요") #newpath변수에 stockcode를 넣을 경로 입력 안내문 저장

if newpath[-1] == '/': #만약 변수 newpath에 마지막이 /로 끝났으면
    newname = newpath + target_file #newname변수에 newpath에 저장한 절대경로 + 파일이름을 저장
else: #마지막이 /로 안끝났으면
    newname = newpath + "/" + target_file #내가 직접 추가하고 저장

try: #시도하쇼
    rename(target_file,newname) #rename은 아까 파일 이름을 저장한 target_file변수의 값을 newname으로 재정의
    print(f"{target_file}->{newname}로 이동되엇습니다") #이름바뀐거 출력
except FileNotFoundError as e: #만약 에러가 나오면 e출력?
    print(e)


