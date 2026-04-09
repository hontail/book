from os import remove #os라이브러리에서 remove함수만 가져옴

target_file = 'stockcode_copy.txt' 
k = input("파일을 삭제하시겠습니까  ")
if k == 'Y':
    remove(target_file)