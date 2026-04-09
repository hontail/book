from os.path import getsize #op.path 라이브러리에서 getsize함수만 가져옴

file1 = 'stockcode.txt' #파일 이름
file2 = 'd:/devlab/py200/img_sample.jpg' #파일경로
file_size1 = getsize(file1) #stockcode파일의 바이트 크기만큼 저장
file_size2 = getsize(file2) #이미지 파일의 바이트 크기만큼 저장

print(f'File Name: {file1}\t File Size: {file_size1}')
print(f'File Name: {file2}\t File Size: {file_size2}')
