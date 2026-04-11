import os, glob #os,glob 라이브러리 호출

folder = 'd:/devlab/py200' #folder변수에 절대경로 저장
file_list = os.listdir(folder) #file_list변수는 os라이브러리의 listdir함수를 사용해서 folder의 모든 파일과 디렉터리 목록을 저장
print(file_list)

files = '*.txt' #files는 모든 텍스트 파일 저장하는 변수
file_list = glob.glob(files) #file_list에 모든 텍스트 파일을 꺼내서 저장
print(file_list)
