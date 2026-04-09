from os import rename

target_file = 'stockcode.txt'
newname = input("새로운 이름을 입력하세요")
rename(target_file,newname)
