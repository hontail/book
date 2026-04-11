import os

target_folder = 'tmp' 
k = input("디렉터리를 제거하시겠습니까")
if k == "네":
    try:
        os.rmdir(target_folder)
        print(f"{target_folder}를 삭제했습니다")
    except Exception as e:
        print(e)
