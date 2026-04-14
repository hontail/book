import shutil
import os

target_folder = 'd:/devlab/py200/tmp' #target_folder는 파일의 절대경로 저장
print(f"{target_folder}하위 모든 디렉터리 및 파일들을 삭제합니다.") #삭제 메시지 출력
for file in os.listdir(target_folder): #tmp폴더의 있는 파일들을 1개씩 꺼내서 file변수에 저장
    print(file) #tmp폴더에 어떤 파일들이 있는지 출력
k = input(f"{target_folder}를 삭제하시겠습니까") 
if k == '네':
    try:
        shutil.rmtree(target_folder) #절대경로에 있는 파일들을 제거
        print(f"{target_folder}의 모든 파일들을 삭제했습니다")
    except Exception as e:
        print(e)
