import time
import mylib

print("5초간 프로그램을 정지합니다")
time.sleep(5)
print("5초가 지나갔습니다")

ret1 = mylib.add_txt("대한민국",'1등')#내가 만든 모듈 mylib 대한민국:1등
ret2 = mylib.reverse(1,2,3)#3,2,1출력
print(ret1)
print(ret2)
