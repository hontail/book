try: #안녕하세요 문 실행 
    print('안녕하세요')
    print(param)

except: #param이 정의되지 않았기 때문에 프린트문 실행하고 종료
    print("예외가 발생했습니다")

else: #print(param)을 주석처리하면 오류가 발생하지 않았기 때문에 else문 실행
    print("예외가 발생하지 않았습니다")
