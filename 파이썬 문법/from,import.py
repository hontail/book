from time import sleep#time모듈에서 sleep함수를 사용할거야
from mypackage import mylib#마이패키지 패키지에서 마이라이브러리 모듈을 사용할거야
from mypackage.mylib import reverse#마이패키지에있는 마이라이브러리에 접근해서 reverse함수를 사용할거야

sleep(1) 
mylib.add_txt("나는",'파이썬이다')
reverse(1,2,3)
